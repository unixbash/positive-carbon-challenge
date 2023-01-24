from flask import Blueprint, request

from models.coffee import Coffee
from server.db import connect
from server.utils import get_list_of_dict

api = Blueprint("api", __name__, template_folder="templates")


@api.route("/api/coffee", methods=["GET"])
def get_product():
    response = {}

    try:
        kwargs = {
            "avg": request.args.get("avg"),  # Rolling average
            "max": request.args.get("max"),  # Max price
            "min": request.args.get("min"),  # Min price
            "changes": request.args.get("changes"),  # Changes over time
        }

        coffee = Coffee()
        connection = connect()
        # Init questdb database
        with connection as conn:
            # Open a cursor to perform database operations
            with conn.cursor() as cur:
                # Query the database and obtain data as Python objects.
                cur.execute(coffee.fetch_query())
                response_data = cur.fetchall()

        # Transform to JSON
        response = get_list_of_dict(coffee.keys, response_data)

    except Exception as e:
        response = (
            f"Unable to return coffee price data due to the following error: {str(e)}"
        )
    finally:
        return response
