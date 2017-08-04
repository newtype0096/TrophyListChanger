"""
This is a setup.py script generated by py2applet

Usage:
    python3 setup.py py2app -A
"""

from setuptools import setup

APP = ['TrophyListChanger_OSX.py']
APP_NAME = '트로피 리스트 변환'
DATA_FILES = []
OPTIONS = {
    'argv_emulation': False,
    'iconfile': 'Logo.icns',
    'includes': ['resource_rc', 'pyperclip'],
    'strip': True,
    'plist': {
        'CFBundleName': APP_NAME,
		'CFBundleDisplayName': APP_NAME,
		'CFBundleGetInfoString': "트로피 리스트 변환 자동화 1.0.4",
		'CFBundleIdentifier': "M-AHHH",
		'CFBundleVersion': "1.0.4",
		'CFBundleShortVersionString': "1.0.4",
		'NSHumanReadableCopyright': "Copyright (C) 2017, M-AHHH, All Rights Reserved"
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
