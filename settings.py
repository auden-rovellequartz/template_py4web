import os

# db settings
APP_FOLDER = os.path.dirname(__file__)
APP_NAME = os.path.split(APP_FOLDER)[-1]

# DB_FOLDER:    Sets the place where migration files will be created
#               and is the store location for SQLite databases
DB_FOLDER = os.path.join(APP_FOLDER, "databases")
DB_URI = "sqlite://storage.db"
DB_POOL_SIZE = 20

# session settings
SESSION_TYPE = "cookies"
SESSION_SECRET_KEY = "<my secret key>"
MEMCACHE_CLIENTS = ["127.0.0.1:11211"]
REDIS_SERVER = "localhost:6379"

# logger settings
LOGGERS = [
    "warning:stdout"
]  # syntax "severity:filename" filename can be stderr or stdout

# enable PAM
USE_PAM = False

# i18n settings
T_FOLDER = os.path.join(APP_FOLDER, "translations")

# try import private settings
try:
    from .settings_private import *
except:
    pass
