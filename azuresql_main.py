# main_app.py
import os
from dotenv import load_dotenv
import pandas as pd
import azuresql_db as sql_db
from prompts.prompts import SYSTEM_MESSAGE, SYSTEM_MESSAGE_1
from azuresql_openai import get_completion_from_messages
import json
from sqlalchemy import create_engine
import pyodbc

load_dotenv()
""" 
connection_string = 'mssql+pyodbc://'+os.getenv('AZURESQL_DB_USERNAME')+':'+os.getenv('AZURESQL_DB_PASSWORD')+'@'+os.getenv('SERVER')+':1433/'+os.getenv('DATABASE')+'?driver=ODBC+Driver+18+for+SQL+Server;encrypt=true;connect_timeout=30'

 """

def detect_duplicate_column_names(df):
  """Detects duplicate column names in a DataFrame.

  Args:
    df: A Pandas DataFrame.

  Returns:
    A list of duplicate column names.
  """

  


def query_database(query):
    # Connect to the database
    connection = pyodbc.connect(sql_db.connection_string)
    df = pd.read_sql_query(sql=query, con=connection)
    return df

# Schema Representation for finances table
schema = sql_db.get_schema()

# Format the system message with the schema
formatted_system_message = SYSTEM_MESSAGE_1.format(schema=schema)
print(formatted_system_message)

# Generate the SQL query from the user message
user_message = "show me courses taken by Gary along with other profile information"

# Use GPT-4 to generate the SQL query
response = get_completion_from_messages(formatted_system_message, user_message)
print(response)

json_response = json.loads(response)
query = json_response['query']
print(query)

# Run the SQL query
sql_results = query_database(query)
print(sql_results)