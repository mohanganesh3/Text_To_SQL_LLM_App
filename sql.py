import sqlite3
connection=sqlite3.connect("student.db")

cursor =connection.cursor()

table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);

"""
cursor.execute(table_info)

cursor.execute('''Insert Into STUDENT values('ganesh','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('rohith','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('karthik','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('sandeep','DEVOPS','A',50)''')
cursor.execute('''Insert Into STUDENT values('Dhanush','DEVOPS','A',35)''')

print("The isnerted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

connection.commit()
connection.close()