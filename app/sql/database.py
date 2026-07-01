from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

from app.config.settings import (
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USERNAME,
    DB_PASSWORD
)

from app.core.exceptions import SQLException


class DatabaseConnection:
    """
    Creates and manages MySQL database connection.
    """

    def __init__(self):

        self.connection_url = (
            f"mysql+pymysql://"
            f"{DB_USERNAME}:{DB_PASSWORD}"
            f"@{DB_HOST}:{DB_PORT}"
            f"/{DB_NAME}"
        )

        self.engine = None

    def connect(
        self
    ) -> Engine:

        try:

            if self.engine is None:

                self.engine = create_engine(
                    self.connection_url,
                    pool_pre_ping=True
                )

            return self.engine

        except Exception as exception:

            raise SQLException(
                "Failed to connect to MySQL database."
            ) from exception