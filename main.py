from numpy import datetime64
import pandas as pd
import sqlalchemy
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
    names=["salesdate", "productid", "region", "freeship", "discount", "itemssold"],
    dtype={
        "salesdate": str,
        "productid": int,
        "region": str,
        "freeship": bool,
        "discount": float,
        "itemssold": int,
    },
    index_col=False,
)

df["salesdate"] = pd.to_datetime(df["salesdate"])


url_object = sqlalchemy.URL.create(
    "mysql+pymysql",
    username=username,
    password=password,
    host=host,
    database=database,
    port=port,
)

engine = sqlalchemy.create_engine(url_object)


df.to_sql("Feature_Store", con=engine, if_exists="append", index=False)

# Read from db
engine.dispose()
