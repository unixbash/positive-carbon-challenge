import time
import requests

from celery import Celery

from server.db import connect
from server import config_module
from server.models.coffee import Coffee

cfg = config_module.DevelopmentConfig  # TODO centralise config selection
celery_app = Celery(broker=cfg.CELERY_BROKER)


@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    """
    Set up a periodic task for every commodity.
    """
    for commodity, update_interval in cfg.COMMODITIES.items():
        commodity_endpoint = (
            f"{cfg.BASE_API_ENDPOINT}/{cfg.DATA_TYPE}"
            f"?access_key={cfg.API_KEY}"
            f"&%20base={commodity}"
            f"&%20symbols={cfg.DEFAULT_CURRENCY}"
        )

        sender.add_periodic_task(update_interval, fetch.s(commodity_endpoint))


@celery_app.task
def fetch(endpoint: str):
    """
    Fetch the info for a given commodity load it into QuestDB.
    """

    coffee = requests.get(endpoint).json()["data"]
    cost = coffee["rates"][cfg.DEFAULT_CURRENCY]

    # Convert datetime into millisecond for QuestDB
    timestamp = time.time_ns() // 1000

    connection = connect()
    with connection as conn:
        # Open a cursor to perform database operations
        with conn.cursor() as cur:
            # Create a new coffee table
            coffee_obj = Coffee()
            cur.execute(coffee_obj.insert_query(), (timestamp, cost))


commodity_endpoint = (
            f"{cfg.BASE_API_ENDPOINT}/{cfg.DATA_TYPE}"
            f"?access_key={cfg.API_KEY}"
            f"&%20base=COFFEE"
            f"&%20symbols={cfg.DEFAULT_CURRENCY}"
        )

while True:
    fetch(commodity_endpoint)
    time.sleep(60)
