# -*- coding: utf-8 -*-


import os

from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

dotenv_path = os.path.join(basedir, ".env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


# The default value can work, if no user config.
LOCAL = os.getenv("local", "en")


# the information of package
__package_name__ = "timestamp"
__version__ = "1.0.7"
__short_description__ = "A time plugin for Flow."
GITHUB_USERNAME = "Zeroto521"
__license__ = 'MIT'


readme_path = os.path.join(basedir, 'README.md')
__long_description__ = open(readme_path, "r").read()


# other information
PLUGIN_ID = "84ddc2a6d43911e8a8d5f2801f1b9fd1"
ICON_PATH = "assets/favicon.ico"
PLUGIN_ACTION_KEYWORD = "ts"
PLUGIN_AUTHOR = "Zeroto521"
PLUGIN_PROGRAM_LANG = "python"
PLUGIN_URL = f"https://github.com/{GITHUB_USERNAME}/Flow.Launcher.Plugin.Timestamp"
PLUGIN_EXECUTE_FILENAME = "main.py"


# time & date split symbol
DATE_SPLIT_SYMBOL = os.getenv('date_split_symbol', '-')
TIME_SPLIT_SYMBOL = os.getenv('time_split_symbol', ':')
