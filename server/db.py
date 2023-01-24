import sys
import psycopg2 as pg
from psycopg2 import OperationalError

import config_module
from models.coffee import Coffee

cfg = config_module.DevelopmentConfig  # TODO centralise config selection


# Connect to database
def connect():
    connection = None
    try:
        connection = pg.connect(cfg.DATABASE_URI)
        connection.autocommit = True
    except OperationalError as err:
        sys.exit(f"Could not connect to the DB with error: {str(err)}")
    finally:
        return connection


# Init database
def init_db():
    connection = connect()
    # Init questdb database
    with connection as conn:
        # Open a cursor to perform database operations
        with conn.cursor() as cur:
            # Create a new coffee table
            coffee_obj = Coffee()
            cur.execute(coffee_obj.init_query())
