import pandas as pd
import sqlalchemy
from sqlalchemy import Column, Integer, MetaData, Table

# pymysql is not explicitly used but needed
import pymysql
import json


with open("credentials.json") as f:
    server_details = json.load(f)

## Assign a new item to `server_details` dictionary
server_details["database"] = "defaultdb"


# Connect to db with pymysql driver
connection_string = sqlalchemy.URL.create("mysql+pymysql", **server_details)
engine = sqlalchemy.create_engine(connection_string)


metadata = MetaData()


eatures = Table(
    "Feature_Store",
    metadata,
    Column("index", Integer, primary_key=True, autoincrement=True),
    Column("salesdate", sqlalchemy.Date),
    Column("productid", Integer),
    Column("region", sqlalchemy.CHAR(4)),
    Column("freeship", sqlalchemy.CHAR(5)),
    Column("discount", sqlalchemy.DECIMAL(3, 2)),
    Column("itemssold", Integer),
)
pd.read_sql("SHOW TABLES;", engine)
metadata.create_all(engine)
