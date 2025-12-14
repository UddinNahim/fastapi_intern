from piccolo.engine.postgres import PostgresEngine
from piccolo.conf.apps import AppRegistry

DB = PostgresEngine(
    config={
        "host": "localhost",
        "database": "flygeracademyDB",
        "user": "nahim",
        "password": "nahim",
        "port": 5434,
    }
)
APP_REGISTRY = AppRegistry(apps=["academy.piccolo_app"])
