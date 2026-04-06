from setuptools import setup

APP = ['gui.py']

DATA_FILES = [
    ('', ['base_lgb.pkl'])
]
 
OPTIONS = {
    'argv_emulation': True,

    # 🔥 Important (hidden imports fix)
    'packages': ['customtkinter', 'pandas', 'numpy', 'joblib', 'lightgbm'],

    # 🔥 GUI apps ke liye required
    'plist': {
        'CFBundleName': 'RSSI Predictor',
        'CFBundleDisplayName': 'RSSI Predictor',
        'CFBundleIdentifier': 'com.rssi.app',
        'CFBundleVersion': '1.0.0',
    },

    # 🔥 Fix missing modules issue
    'includes': ['tkinter'],

    # 🔥 Better compatibility
    'excludes': ['matplotlib', 'scipy']
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
