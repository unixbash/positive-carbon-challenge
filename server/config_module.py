class Config(object):
    """Default system config"""

    TESTING = False
    DEBUG = False
    FLASK_RUN_PORT = 5005

    """ Celery settings """
    CELERY_HOST = "localhost"
    CELERY_PORT = 6379
    CELERY_BROKER: str = f"redis://{CELERY_HOST}:{CELERY_PORT}/0"

    """ DB connection info """
    DB_HOST = "localhost"
    DB_PORT = 8812
    DB_TABLE = "qdb"
    DB_USER = "admin"
    DB_PASS = "quest"  # TODO Hash plaintext password using something like bcrypt

    DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_TABLE}"

    """ Commodities API endpoint info """
    BASE_API_ENDPOINT = "https://commodities-api.com/api"
    DATA_TYPE = (
        "latest"  # NOTE With the free subscription plan data updates every 60 minutes
    )
    API_KEY = "w5zq8c54w25ujsbmwcol224kapgmobgmsai1zo0qfd47np59becae4i2b80y"
    COMMODITIES = {"COFFEE": 60}  # Update interval in seconds
    DEFAULT_CURRENCY = "EUR"


class DevelopmentConfig(Config):
    """Enable debug mode"""

    DEBUG = True


class ProductionConfig(Config):
    """Uses production database server."""

    DB_HOST = "1.2.3.4"


class TestConfig(Config):
    """Uses test database server."""

    TESTING = True
    DEBUG = True
    DB_HOST = "4.3.2.1"
