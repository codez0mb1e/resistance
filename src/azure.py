
# %% Import dependencies ----
from dataclasses import dataclass
from typing import Dict, Any, Iterable
from pandas import DataFrame
from sqlalchemy import create_engine, inspect
import urllib


# %%
@dataclass(frozen=True)
class ConnectionSettings:
    """Connection Settings."""
    server: str
    database: str
    username: str
    password: str
    driver: str = '{ODBC Driver 17 for SQL Server}'
    timeout: int = 30


class AzureDbConnection:
    """
    Azure SQL database connection.
    """
    def __init__(self, conn_settings: ConnectionSettings, echo: bool = False) -> None:
        conn_params = urllib.parse.quote_plus(
            'Driver=%s;' % conn_settings.driver +
            'Server=tcp:%s,1433;' % conn_settings.server +
            'Database=%s;' % conn_settings.database +
            'Uid=%s;' % conn_settings.username +
            'Pwd={%s};' % conn_settings.password +
            'Encrypt=yes;' +
            'TrustServerCertificate=no;' +
            'Connection Timeout=%s;' % conn_settings.timeout
        )
        conn_string = f'mssql+pyodbc:///?odbc_connect={conn_params}'

        self.db = create_engine(conn_string, echo=echo)

    def connect(self) -> None:
        """Estimate connection."""
        self.conn = self.db.connect()

    def get_tables(self) -> Iterable[str]:
        """Get list of tables."""
        inspector = inspect(self.db)
        return [t for t in inspector.get_table_names()]

    def insert(self, inserted_data: DataFrame, target_table: str, db_mapping: Dict[str, Any], chunksize: int = 10000) -> None:
        inserted_data.to_sql(
            con=self.db,
            schema='dbo',
            name=target_table,
            if_exists='append',  # or replace
            index=False,
            chunksize=chunksize,
            dtype=db_mapping
        )

    def dispose(self) -> None:
        """Dispose opened connections."""
        self.conn.close()
        self.db.dispose()
