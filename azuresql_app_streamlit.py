# main_app.py

import streamlit as st
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

#connection_string = 'mssql+pyodbc://'+os.getenv('AZURESQL_DB_USERNAME')+':'+os.getenv('AZURESQL_DB_PASSWORD')+'@'+os.getenv('SERVER')+':1433/'+os.getenv('DATABASE')+'?driver=ODBC+Driver+18+for+SQL+Server;encrypt=true;connect_timeout=30'

def query_database(query):
    # Connect to the database
    connection = pyodbc.connect(sql_db.connection_string)
    df = pd.read_sql_query(sql=query, con=connection)
    return df 


# Schema Representation for finances table
schema = sql_db.get_schema()

st.set_page_config(layout="wide")
st.title("Query Your SQL Data with GPT-4")
st.write("Enter your message to view results.")

# Input field for the user to type a message
user_message = st.text_input("Enter your message:")

if user_message:
    # Format the system message with the schema
    formatted_system_message = SYSTEM_MESSAGE_1.format(schema=schema)
    print("before call to openai")
    print(formatted_system_message)
    print(user_message)
    # Use GPT-4 to generate the SQL query
    response = get_completion_from_messages(formatted_system_message, user_message)
    json_response = json.loads(response)
    query = json_response['query']
    
    # Display the generated SQL query
    st.write("Generated SQL Query:")
    st.code(query, language="sql")
    print("before executing sql")
    try:
        # Run the SQL query and display the results
        print(query)
        sql_results = query_database(query)
        container = st.container()

        # Display some text inside the expander
        with container:
            st.write("Query Results:")
            st.dataframe(sql_results)

    except Exception as e:
        st.write(f"An error occurred: {e}")
