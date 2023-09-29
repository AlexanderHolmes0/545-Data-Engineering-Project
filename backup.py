import pandas as pd
import sqlalchemy
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


url_object = sqlalchemy.URL.create(
    "mysql+pymysql",
    username=username,
    password=password,
    host=host,
    database=database,
    port=port,
)

engine = sqlalchemy.create_engine(url_object)

pd.read_sql("SELECT * FROM Feature_Store;", engine).to_csv("backup.csv", index=False)

engine.dispose()
