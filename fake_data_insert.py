import pyodbc
from faker import Faker
import os
from dotenv import load_dotenv

load_dotenv()

# Set up a connection to SQL Server
connection_string = 'Driver={ODBC Driver 18 for SQL Server};Server=tcp:'+os.getenv('SERVER')+',1433;Database='+os.getenv('DATABASE')+';Uid='+os.getenv('AZURESQL_DB_USERNAME')+';Pwd='+os.getenv('AZURESQL_DB_PASSWORD')+';Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'

# Connect to the database
conn = pyodbc.connect(connection_string)

# Create a cursor
cursor = conn.cursor()

# Create an instance of the Faker library
fake = Faker()

# List of college names, payment plans, and semesters for random selection
CampusName = ['Campus A', 'Campus B', 'Campus C', 'Campus D']
payment_plans = ['Monthly', 'Quarterly', 'Semesterly']
semesters = ['Fall', 'Spring', 'Winter']

# Generate and insert random records
for student_id in range(1508, 6000):
    college_name = fake.random.choice(CampusName)
    tuition_fees = fake.pyfloat(left_digits=5, right_digits=2, positive=True)
    room_board_fees = fake.pyfloat(left_digits=5, right_digits=2, positive=True)
    books_supplies = fake.pyfloat(left_digits=5, right_digits=2, positive=True)
    scholarship_amount = fake.pyfloat(left_digits=5, right_digits=2, positive=True)
    federal_aid_amount = fake.pyfloat(left_digits=5, right_digits=2, positive=True)
    state_aid_amount = fake.pyfloat(left_digits=5, right_digits=2, positive=True)
    outstanding_balance = tuition_fees + room_board_fees + books_supplies - scholarship_amount - federal_aid_amount - state_aid_amount
    payment_plan = fake.random.choice(payment_plans)
    semester = fake.random.choice(semesters)

    cursor.execute(
        '''
        INSERT INTO dbo.StudentAccount (
            StudentID, CampusName, TuitionFees, RoomBoardFees, BooksSupplies,
            ScholarshipAmount, FederalAidAmount, StateAidAmount, OutstandingBalance,
            PaymentPlan, Semester
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        student_id, college_name, tuition_fees, room_board_fees, books_supplies,
        scholarship_amount, federal_aid_amount, state_aid_amount, outstanding_balance,
        payment_plan, semester
    )

cursor.close()

# Commit the transaction
conn.commit()

# Close the connection
conn.close()
