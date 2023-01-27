from sqlalchemy import create_engine, text
import pandas as pd
import os

def get_sql_file_path(sql_filename: str):
    project_dir = os.path.dirname(os.path.abspath(''))
    sql_path = os.path.join(project_dir, "sql", sql_filename)
    
    return sql_path

def get_sql_query(sql_filename: str):
    sql_file_path = get_sql_file_path(sql_filename)
    f = open(sql_file_path, 'r')
    sql_statement = f.read()
    f.close()

    return sql_statement

def get_dataframe(sql_filename: str, conn_string: str):
    sql_query = get_sql_query(sql_filename)

    print(sql_query)

    # Create an engine instance
    alchemyEngine = create_engine(conn_string, pool_recycle=3600);

    # Connect to PostgreSQL server
    dbConnection = alchemyEngine.connect();

    # Read data from PostgreSQL database table and load into a DataFrame instance
    df = pd.read_sql(text(sql_query), dbConnection);

    # Close the database connection
    dbConnection.close();

    return df