import random
from faker import Faker
import pyodbc 
import os
from dotenv import load_dotenv

load_dotenv()

fake = Faker()

connection_string = 'Driver={ODBC Driver 18 for SQL Server};Server=tcp:'+os.getenv('SERVER')+',1433;Database='+os.getenv('DATABASE')+';Uid='+os.getenv('AZURESQL_DB_USERNAME')+';Pwd='+os.getenv('AZURESQL_DB_PASSWORD')+';Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'


# Connect to your Azure SQL database
conn = pyodbc.connect(connection_string)

cursor = conn.cursor()

# Generate fake data for StudentProfile table
for student_id in range(1, 101):
    cursor.execute("""
        INSERT INTO StudentProfile (StudentID, FirstName, LastName, DateOfBirth, Gender)
        VALUES (?, ?, ?, ?, ?)
    """, (
        student_id,  # StudentID
        fake.first_name(),  # FirstName
        fake.last_name(),  # LastName
        fake.date_of_birth(minimum_age=18, maximum_age=25).strftime('%Y-%m-%d'),  # DateOfBirth
        fake.random.choice(['Male', 'Female'])  # Gender
    ))

# Generate fake data for StudentAcademic table
for academic_id in range(1, 101):
    cursor.execute("""
        INSERT INTO StudentAcademic (AcademicID, StudentID, Major, GPA, CreditsEarned, Program, Semester, StartDate)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        academic_id,  # AcademicID
        academic_id,  # StudentID
        fake.random.choice(['Computer Science', 'Mathematics', 'Physics']),  # Major
        round(random.uniform(2.0, 4.0), 2),  # GPA
        fake.random_int(min=30, max=120),  # CreditsEarned
        fake.random.choice(['Undergraduate', 'Graduate']),  # Program
        fake.random.choice(['Fall', 'Spring', 'Summer']),  # Semester
        fake.date_between(start_date='-4y', end_date='today').strftime('%Y-%m-%d')  # StartDate
    ))

# Generate fake data for StudentAccounting table
for accounting_id in range(1, 101):
    cursor.execute("""
        INSERT INTO StudentAccounting (AccountingID, StudentID, TuitionDue, BookFee, RoomFee, FinancialAid, Scholarship, Balance)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        accounting_id,  # AccountingID
        accounting_id,  # StudentID
        round(random.uniform(5000.00, 20000.00), 2),  # TuitionDue
        round(random.uniform(200.00, 1000.00), 2),  # BookFee
        round(random.uniform(1000.00, 5000.00), 2),  # RoomFee
        round(random.uniform(0.00, 5000.00), 2),  # FinancialAid
        round(random.uniform(0.00, 5000.00), 2),  # Scholarship
        round(random.uniform(0.00, 5000.00), 2)  # Balance
    ))

# Generate fake data for Courses table
for course_id in range(101, 301):
    cursor.execute("""
        INSERT INTO Courses (CourseID, AcademicID, Program, CourseName, CourseCode, Credits, SemesterOffered)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        course_id,  # CourseID
        fake.random_int(min=1, max=100),  # AcademicID (randomly associating courses with academic records)
        fake.random.choice(['Undergraduate', 'Graduate']),  # Program
        fake.bs(),  # CourseName
        fake.bothify(text='???###'),  # CourseCode
        fake.random_int(min=1, max=4),  # Credits
        fake.random.choice(['Fall', 'Spring', 'Summer'])  # SemesterOffered
    ))

conn.commit()
cursor.close()
conn.close()
