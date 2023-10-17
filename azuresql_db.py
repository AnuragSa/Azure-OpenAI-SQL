import pyodbc

# Get your Azure SQL Database connection information
server = 'anurag-ai-demo-db.database.windows.net'
database = 'azurag-ai-demo-database'
username = 'anuragadmin'
password = ''

# Create a connection string
connection_string = 'Driver={ODBC Driver 18 for SQL Server};Server=tcp:anurag-ai-demo-db.database.windows.net,1433;Database=azurag-ai-demo-database;Uid=anuragadmin;Pwd='+password+';Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'

# Connect to the database
connection = pyodbc.connect(connection_string)

# Create a cursor
cursor = connection.cursor()

# Execute a SQL query
cursor.execute('SELECT * FROM StudentData')

# Retrieve the results of the query
results = cursor.fetchall()
print(results)

# Close the cursor and connection
cursor.close()
connection.close()
