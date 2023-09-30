from numpy import datetime64
import pandas as pd
import sqlalchemy
from sqlalchemy import Column, Integer, MetaData, Table, text

# pymysql is not explicitly used but needed
import pymysql
import os
import sys
import requests


def exit_program():
    print("Exiting the program...")
    sys.exit(0)


try:
    username = os.environ["API_USER"]
    password = os.environ["API_PASSWORD"]
    port = os.environ["PORT"]
    host = os.environ["HOST"]
    database = os.environ["DB"]
except KeyError:
    SOME_SECRET = "Token not available!"


url_object = sqlalchemy.URL.create(
    "mysql+pymysql",
    username=username,
    password=password,
    host=host,
    database=database,
    port=port,
)

engine = sqlalchemy.create_engine(url_object)


con = engine.connect()  # connect to db


try:
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

    if df.empty:
        print("Dataframe is empty, exiting program...")
        con.execute(
            text(
                "INSERT into Feature_Store (salesdate, error_code) VALUES (DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY), 'Dataframe is empty')"
            )
        )
        con.commit()
        exit_program()

    df["salesdate"] = pd.to_datetime(df["salesdate"])

    max_date_in_DB = (
        pd.read_sql("SELECT max(salesdate) FROM Feature_Store;", engine)
        .at[0, "max(salesdate)"]
        .strftime("%Y-%m-%d")
    )

    if max_date_in_DB == max(df["salesdate"]).strftime("%Y-%m-%d"):
        print("No new data to add")
        con.execute(
            text(
                "INSERT into Feature_Store (salesdate, error_code) VALUES (DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY), 'No new data to add')"
            )
        )
        con.commit()
    elif max_date_in_DB > max(df["salesdate"]).strftime("%Y-%m-%d"):
        print("New data is older than existing data")
        con.execute(
            text(
                "INSERT into Feature_Store (salesdate, error_code) VALUES (DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY), 'New data is older than existing data')"
            )
        )
        con.commit()
    elif max_date_in_DB < max(df["salesdate"]).strftime("%Y-%m-%d"):
        print("New data is newer than existing data")
        df.to_sql("Feature_Store", con=engine, if_exists="append", index=False)
        print("New data added")

except:
    x = (
        "Request Code: "
        + requests.get(
            "https://raw.githubusercontent.com/AdamSpannbauer/rand-daily-records/master/yesterdays-records.txt"
        ).status_code.__str__()
    )
    con.execute(
        text(
            "INSERT into Feature_Store (salesdate, error_code) VALUES (DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY), :x)"
        ).bindparams(x=x)
    )
    con.commit()


# Read from db
engine.dispose()
