import configparser
import os

DEFAULT_CONFIGURATION_FILE = "tagger/database.cfg"

config = configparser.ConfigParser()
config.read(DEFAULT_CONFIGURATION_FILE)
