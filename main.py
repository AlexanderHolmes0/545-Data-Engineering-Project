from numpy import datetime64
import pandas as pd
import json
import sqlalchemy as chem
from sqlalchemy import Column, Integer, MetaData, Table

# pymysql is not explicitly used but needed
import pymysql
import os

try:
    username = os.environ["API_USER"]
    password = os.environ["API_PASSWORD"]
    port = os.environ["PORT"]
    host = os.environ["HOST"]
    database = os.environ["DB"]
except KeyError:
    SOME_SECRET = "Token not available!"


df = pd.read_table(
    "https://raw.githubusercontent.com/AdamSpannbauer/rand-daily-records/master/yesterdays-records.txt",
    delimiter=",",
    names=["Created", "Value1", "Value2", "Value3", "Value4", "Value5"],
    dtype={
        "Created": str,
        "Value1": int,
        "Value2": str,
        "Value3": bool,
        "Value4": float,
        "Value5": int,
    },
    index_col=False,
)

df["Created"] = pd.to_datetime(df["Created"])

# Connect to db with pymysql driver

connection_string = chem.URL.create(
    "mysql+pymysql",
    username=username,
    password=password,
    host=host,
    port=port,
    database=database,
)
engine = chem.create_engine(connection_string)

df.to_sql("Feature_Store", con=engine, if_exists="append", index=False)


# Tidy up
engine.dispose()
