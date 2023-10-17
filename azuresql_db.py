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
connection_string = 'Driver={ODBC Driver 18 for SQL Server};Server=tcp:anurag-ai-demo-db.database.windows.net,1433;Database=azurag-ai-demo-database;Uid='+username+';Pwd='+password+';Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'

# Connect to the database
connection = pyodbc.connect(connection_string)

# Create a cursor
cursor = connection.cursor()

cursor.execute("SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'StudentData'")

db_schema = cursor.fetchall()
print(db_schema)
'''
db_schema = {}

for table in tables:
    table_name = table[0]
    
    # Query to get column details for each table
    cursor.execute(f"PRAGMA table_info({table_name});")
    columns = cursor.fetchall()
    
    column_details = {}
    for column in columns:
        column_name = column[1]
        column_type = column[2]
        column_details[column_name] = column_type
    
    db_schema[table_name] = column_details
'''
cursor.close()    
connection.close()




