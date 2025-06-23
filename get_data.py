import snowflake.connector
from dotenv import load_dotenv
import os

def get_snowflake_connection():
    load_dotenv()
    user = os.getenv("SNOWFLAKE_USER")
    password = os.getenv("SNOWFLAKE_PASSWORD")
    role = os.getenv("SNOWFLAKE_ROLE")
    warehouse = os.getenv("SNOWFLAKE_WAREHOUSE")
    database = os.getenv("SNOWFLAKE_DATABASE")
    schema = os.getenv("SNOWFLAKE_SCHEMA")
    account = os.getenv("SNOWFLAKE_ACCOUNT")
    conn = snowflake.connector.connect(
        user=user,
        password=password,
        account=account,
        warehouse=warehouse,
        database=database,
        schema=schema,
        role=role
    )
    return conn

def get_data(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM dev.mart_price;")
    df = cur.fetch_pandas_all()
    cur.close()
    return df

def get_mart_production_data(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM dev.mart_production;")
    df = cur.fetch_pandas_all()
    cur.close()
    return df

def get_mart_price_data(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM dev.mart_price;")
    df = cur.fetch_pandas_all()
    cur.close()
    return df
    

if __name__ == "__main__":
    con = get_snowflake_connection()
    df = get_mart_production_data(con)
    df_price = get_mart_price_data(con)
    con.close()
    print(df_price.head(10))