from flask import Flask
from flask_cors import CORS
from werkzeug.utils import import_string
from db import init_db
from api import api

# Application config
cfg = import_string("config_module.DevelopmentConfig")()
app = Flask(__name__)
app.config.from_object(cfg)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"


# Register blueprints
app.register_blueprint(api)

# Init database
init_db()

if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"], test=app.config["TEST"])
