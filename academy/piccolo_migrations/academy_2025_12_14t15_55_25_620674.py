from piccolo.apps.migrations.auto.migration_manager import MigrationManager
from piccolo.columns.column_types import Decimal
from piccolo.columns.column_types import Integer
from piccolo.columns.column_types import Timestamptz
from piccolo.columns.defaults.timestamptz import TimestamptzCustom
import decimal


ID = "2025-12-14T15:55:25:620674"
VERSION = "1.30.0"
DESCRIPTION = ""


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="academy", description=DESCRIPTION
    )

    manager.alter_column(
        table_class_name="Course",
        tablename="course",
        column_name="price",
        db_column_name="price",
        params={"default": decimal.Decimal("0"), "digits": None},
        old_params={"default": 0, "digits": None},
        column_class=Decimal,
        old_column_class=Integer,
        schema=None,
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
                hour=9,
                minute=55,
                second=25,
                microsecond=618122,
            )
        },
        old_params={
            "default": TimestamptzCustom(
                year=2025,
                month=12,
                day=14,
                hour=4,
                minute=3,
                second=57,
                microsecond=573980,
            )
        },
        column_class=Timestamptz,
        old_column_class=Timestamptz,
        schema=None,
    )

    return manager
