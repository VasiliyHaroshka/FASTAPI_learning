from model.user import User
from error import Duplicate, Missing
from .init import curs, get_db, IntegrityError

curs.execute("""
    CREATE TABLE IF NOT EXISTS 
    User(
    name text PRIMARY KEY,
    hash text
    )""")

curs.execute("""
    CREATE TABLE IF NOT EXISTS 
    XUser(
    name text PRIMARY KEY,
    hash text
    )""")
