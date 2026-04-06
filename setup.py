from setuptools import setup

APP = ['gui.py']

DATA_FILES = [
    ('', ['base_lgb.pkl'])
]

OPTIONS = {
    'argv_emulation': True,
    'packages': ['customtkinter', 'pandas', 'numpy', 'joblib', 'lightgbm'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
