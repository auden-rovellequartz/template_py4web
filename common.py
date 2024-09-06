"""
This file defines cache, session, and translator T object for the app
These are fixtures that every app needs so probably you will not be editing this file
"""
from .modules.external_imports import *
from py4web import Session, Cache, Translator, DAL, Field, action, request, abort, redirect, URL
from py4web.utils.auth import Auth
from py4web.utils.factories import ActionFactory
from py4web.utils.mailer import Mailer
from pydal.tools.tags import Tags
from py4web.utils.form import Form
from . import settings

# implement custom loggers form settings.LOGGERS
logger = logging.getLogger("py4web:" + settings.APP_NAME)
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s"
)
for item in settings.LOGGERS:
    level, filename = item.split(":", 1)
    if filename in ("stdout", "stderr"):
        handler = logging.StreamHandler(getattr(sys, filename))
    else:
        handler = logging.FileHandler(filename)
    handler.setLevel(getattr(logging, level.upper(), "ERROR"))
    handler.setFormatter(formatter)
    logger.addHandler(handler)

# connect to db
db = DAL(settings.DB_URI, folder=settings.DB_FOLDER, pool_size=settings.DB_POOL_SIZE)

# define global objects that may or may not be used by th actions
cache = Cache(size=1000)
T = Translator(settings.T_FOLDER)

# pick the session type that suits you best
if settings.SESSION_TYPE == "cookies":
    session = Session(secret=settings.SESSION_SECRET_KEY)
elif settings.SESSION_TYPE == "redis":
    import redis

    host, port = settings.REDIS_SERVER.split(":")
    # for more options: https://github.com/andymccurdy/redis-py/blob/master/redis/client.py
    conn = redis.Redis(host=host, port=int(port))
    conn.set = lambda k, v, e, cs=conn.set, ct=conn.ttl: cs(k, v, ct(k)) if ct(k) >= 0 else cs(k, v, e) 
    session = Session(secret=settings.SESSION_SECRET_KEY, storage=conn)
elif settings.SESSION_TYPE == "memcache":
    import memcache, time

    conn = memcache.Client(settings.MEMCACHE_CLIENTS, debug=0)
    session = Session(secret=settings.SESSION_SECRET_KEY, storage=conn)
elif settings.SESSION_TYPE == "database":
    from py4web.utils.dbstore import DBStore

    session = Session(secret=settings.SESSION_SECRET_KEY, storage=DBStore(db))





