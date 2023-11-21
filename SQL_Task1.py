#Q1. What is a database? Differentiate between SQL and NoSQL databases.
#Ans. A database is a structured collection of data that is organized and stored in a way that allows for efficient retrieval and management. Databases are used to store, manage, and retrieve information for various applications and systems.
#SQL: SQL databases are relational databases, meaning they use a structured format based on tables with rows and columns. They follow a fixed schema, and data is organized in a tabular format.
#NoSQL databases can have various data models, including document-oriented, key-value pairs, wide-column stores, and graph databases. They offer more flexibility in handling different types of data.


#Q2. What is DDL? Explain why CREATE, DROP, ALTER, and TRUNCATE are used with an example.
#Ans. DDL is a subset of SQL (Structured Query Language) that deals with the structure and definition of the database objects. It includes statements for creating, altering, and deleting database objects such as tables, indexes, and schemas.
#The CREATE statement is used to create new database objects, such as tables, indexes, or views.
#The DROP statement is used to delete existing database objects, such as tables or indexes.
#The ALTER statement is used to modify the structure of existing database objects, such as tables.
#The TRUNCATE statement is used to remove all rows from a table while retaining the table structure for future use. It is faster than the DELETE statement for removing all rows.
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE if not exists task")
mycursor.execute("USE task")
mycursor.execute("CREATE TABLE if not exists task_table(b1 INT, b2 VARCHAR(40), b3 INT)")
mycursor.execute("TRUNCATE TABLE task_table")
mycursor.execute("ALTER TABLE task_table DROP COLUMN b2")
mydb.close()


#Q3. What is DML? Explain INSERT, UPDATE, and DELETE with an example.
#DML (Data Manipulation Language): DML is a subset of SQL (Structured Query Language) that deals with the manipulation of data stored in a database. It includes statements for inserting, updating, and deleting data within database tables.
#The INSERT statement is used to add new records (rows) into a table.
#The UPDATE statement is used to modify existing records in a table.
# The DELETE statement is used to remove records from a table.
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE if not exists task1")
mycursor.execute("USE task1")
mycursor.execute("CREATE TABLE if not exists task1_table(a1 INT, a2 VARCHAR(40), a3 INT)")
mycursor.execute("INSERT INTO task1_table (a1,a2,a3) VALUES (23, 'ABHI', 25)")
mycursor.execute("UPDATE task1_table SET a1=65 WHERE a2 = 'ABHI'")
mycursor.execute("DELETE FROM task1_table WHERE a3 = 25")
mydb.close()


#Q4. What is DQL? Explain SELECT with an example.
#Ans. DQL is a subset of SQL (Structured Query Language) that deals specifically with the retrieval of data from a database. The primary statement in DQL is the SELECT statement, which allows you to query and retrieve data from one or more tables.
#The SELECT statement is used to retrieve data from one or more tables in a database.
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE if not exists task2")
mycursor.execute("USE task2")
mycursor.execute("CREATE TABLE if not exists task2_table(d1 INT, d2 VARCHAR(40), d3 INT)")
mycursor.execute("SELECT* FROM task2_table")
mydb.close()


#Q5. Explain Primary Key and Foreign Key.
#Ans. A primary key is a unique identifier for a record in a database table. It uniquely identifies each row in the table and ensures that there are no duplicate values.
#A foreign key is a column or a set of columns in a table that refers to the primary key of another table. It establishes a link between the two tables and is used to enforce referential integrity.


#Q6. Write a python code to connect MySQL to python. Explain the cursor() and execute() method.
#Ans. mycursor = mydb.cursor() creates a cursor object (mycursor) that allows you to interact with the database.
#mycursor.execute() is used to execute SQL statements. The SQL statements can include operations like creating tables, inserting data, selecting data, etc.
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE if not exists task2")
mydb.close()


#Q7. Give the order of execution of SQL clauses in an SQL query.
#Ans. The order of execution of SQL clauses in an SQL query generally follows a specific sequence:
#SELECT: This clause specifies the columns to be retrieved from the database.
#FROM: Specifies the table or tables from which the data is to be retrieved.
#WHERE: Filters the rows returned by the SELECT clause based on a specified condition.
#GROUP BY: Groups the rows that have the same values in specified columns into summary rows.
#HAVING: Filters the results of the GROUP BY clause based on a specified condition.
#ORDER BY: Sorts the result set based on one or more columns.
#LIMIT/OFFSET: Limits the number of rows returned or skips a specified number of rows.