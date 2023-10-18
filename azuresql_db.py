import os
from dotenv import load_dotenv
import pyodbc



load_dotenv()

# Get your Azure SQL Database connection information
server = os.getenv('SERVER')
database = os.getenv('DATABASE')
username = os.getenv('AZURESQL_DB_USERNAME')
password = os.getenv('AZURESQL_DB_PASSWORD')

# Create a connection string
connection_string = 'Driver={ODBC Driver 18 for SQL Server};Server=tcp:'+server+',1433;Database='+database+';Uid='+username+';Pwd='+password+';Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'

def get_schema():


    # Connect to the database
    connection = pyodbc.connect(connection_string)

    # Create a cursor
    cursor = connection.cursor()

    cursor.execute("SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'StudentData'")

    db_schema = cursor.fetchall()

    cursor.close()    
    connection.close()
    return db_schema



