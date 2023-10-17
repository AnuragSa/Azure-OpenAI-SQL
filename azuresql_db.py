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

cursor.close()    
connection.close()




