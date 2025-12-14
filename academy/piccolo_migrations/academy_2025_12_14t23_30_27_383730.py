from piccolo.apps.migrations.auto.migration_manager import MigrationManager
from piccolo.columns.column_types import Timestamptz
from piccolo.columns.defaults.timestamptz import TimestamptzCustom


ID = "2025-12-14T23:30:27:383730"
VERSION = "1.30.0"
DESCRIPTION = ""


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="academy", description=DESCRIPTION
    )

    manager.alter_column(
        table_class_name="Course",
        tablename="course",
        column_name="created_on",
        db_column_name="created_on",
        params={
            "default": TimestamptzCustom(
                year=2025,
                month=12,
                day=14,
                hour=17,
                minute=30,
                second=27,
                microsecond=381736,
            )
        },
        old_params={
            "default": TimestamptzCustom(
                year=2025,
                month=12,
                day=14,
                hour=9,
                minute=55,
                second=25,
                microsecond=618122,
            )
        },
        column_class=Timestamptz,
        old_column_class=Timestamptz,
        schema=None,
    )

    return manager
