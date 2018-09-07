"""
run.py
"""
import os

from app import create_app

CONFIGNAME = os.getenv('APP_SETTINGS') # CONFIGNAME = "development"
APP = create_app(CONFIGNAME)

if __name__ == '__main__':
    APP.run()
