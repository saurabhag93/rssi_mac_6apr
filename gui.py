import sys
import os
import joblib
import customtkinter as ctk
import pandas as pd
import numpy as np
from tkinter import messagebox 

# ----------------- Resource helper -----------------
def resource_path(rel_path):
    if getattr(sys, "frozen", False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(base_path, rel_path)

# ----------------- Load model -----------------
MODEL_PATH = resource_path("base_lgb.pkl")

try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    messagebox.showerror("Model Error", f"{e}")
    raise SystemExit

# ----------------- UI -----------------
ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.title("RSSI Predictor")
app.geometry("500x600")

entries = []
labels = ["TxLat","TxLon","RxLat","RxLon","TxH","RxH","TxPower","Freq"]

for l in labels:
    ctk.CTkLabel(app, text=l).pack()
    e = ctk.CTkEntry(app)
    e.pack()
    entries.append(e)

# ----------------- Prediction -----------------
result = ctk.CTkLabel(app, text="")
result.pack(pady=10)

def predict():
    try:
        vals = [float(e.get()) for e in entries]
    except:
        messagebox.showerror("Error","Invalid input")
        return

    TxLat, TxLon, RxLat, RxLon, TxH, RxH, TxP, Freq = vals

    df = pd.DataFrame([{
        "TxLat":TxLat,"TxLon":TxLon,
        "RxLat":RxLat,"RxLon":RxLon,
        "TxHeight_m":TxH,"RxHeight_m":RxH,
        "TxPower_dBm":TxP,"Frequency_MHz":Freq
    }])

    df["Distance_m"] = 1000  # simple placeholder

    X = df.to_numpy()
    pred = model.predict(X)[0]

    result.configure(text=f"RSSI: {pred:.2f} dBm")

ctk.CTkButton(app, text="Predict", command=predict).pack(pady=20)

app.mainloop()
