import mysql.connector

# mydb = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "Parihar_2003"
# )

# myCursor = mydb.cursor();

# myCursor.execute("CREATE DATABASE college");

# myCursor.execute("USE college");

# myCursor.execute("""
#     CREATE TABLE student(
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         name VARCHAR(50),
#         age INT NOT NULL
#     )
# """)

# sql = "INSERT INTO student (id, name, age) VALUES (%s, %s, %s)"
# values = (1, 'Shruti', 22);

# values = [
#     (2, 'Abhishek', 19),
#     (3, 'Aditi', 21)
# ]

# myCursor.executemany(sql, values);
# mydb.commit();

# myCursor.execute("SELECT * FROM student");
# rows = myCursor.fetchall();
# for row in rows:
#     print(row)

# myCursor.execute("DROP TABLE student");

# myCursor.execute("""
#     CREATE TABLE student(
#         id INT PRIMARY KEY,
#         name VARCHAR(50)
#     )    
# """)

# sql = "INSERT INTO student (id, name) VALUES(%s, %s)"
# values = [
#     (1, 'Shruti'),
#     (2, 'Abhishek'),
#     (3, 'Aditi'),
#     (4, 'Ravi')
# ]

# myCursor.executemany(sql, values);

# myCursor.execute("SELECT * FROM student");
# tabs = myCursor.fetchall();
# print("Rows fetched:", len(tabs))
# for tab in tabs:
#     print(f"ID: {tab[0]}, Name: {tab[1]}")


# mydb = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "Parihar_2003"
# )

# myCursor = mydb.cursor();

# myCursor.execute("CREATE DATABASE my_company");

# myCursor.execute("USE my_company");

# myCursor.execute("""
#     CREATE TABLE employee(
#     id INT PRIMARY KEY,
#     name VARCHAR(50),
#     salary INT
#     )
# """)

# ins = "INSERT INTO employee (id, name, salary) VALUES (%s, %s, %s)";
# values = [
#     (1, 'adam', 25000),
#     (2, 'bob', 30000),
#     (3, 'casey', 40000)
# ]

# myCursor.executemany(ins, values);
# myCursor.execute("SELECT * FROM employee");
# tabs = myCursor.fetchall();
# print("Rows fetched:", len(tabs))
# for tab in tabs:
#     print(f"ID: {tab[0]}, Name: {tab[1]}, Salary: {tab[2]}")

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Parihar_2003"
)

myCursor = mydb.cursor();

# myCursor.execute("CREATE DATABASE college");

myCursor.execute("USE COLLEGE");

# myCursor.execute("""
#     CREATE TABLE student(
#         rollno INT PRIMARY KEY,
#         name VARCHAR(50),
#         marks INT NOT NULL,
#         grade VARCHAR(1),
#         city VARCHAR(20))
# """)

# myCursor.execute("""
#     CREATE TABLE dept(
#     id INT PRIMARY KEY,
#     name VARCHAR(50))
# """)

# myCursor.execute("""
#     CREATE TABLE teacher(
#         id INT PRIMARY KEY,
#         name VARCHAR(50),
#         dept_id INT,
#         FOREIGN KEY (dept_id) REFERENCES dept(id))
# """)

# sql = "INSERT INTO student (rollno, name, marks, grade, city) VALUES (%s, %s, %s, %s, %s)";
# values = [
#     (101, 'Anil', 78, 'C', 'Pune'),
#     (102, 'Bhoomika', 93, 'A', 'Mumbai'),
#     (103, 'Chetan', 85, 'B', 'Mumbai'),
#     (104, 'Dhruv', 96, 'A', 'Delhi'),
#     (105, 'Emanuel', 12, 'F', 'Delhi'),
#     (106, 'Farah', 82, 'B', 'Delhi')
# ]


sql = "INSERT INTO dept (id, name) VALUES (101, 'English')";
myCursor.execute(sql);
sql = "INSERT INTO dept (id, name) VALUES (102, 'IT')";
myCursor.execute(sql);
myCursor.execute("SELECT * from dept");
rows = myCursor.fetchall();
for row in rows:
    print(row)

sql = "INSERT INTO teacher (id, name,dept_id) VALUES (101, 'Adam', 101)";
myCursor.execute(sql);
sql = "INSERT INTO teacher (id, name, dept_id) VALUES (102, 'Eve', 102)";
myCursor.execute(sql);
myCursor.execute("SELECT * from teacher");
rows = myCursor.fetchall();
for row in rows:
    print(row)


# myCursor.execute("SELECT city, AVG(marks) from student GROUP BY city ORDER BY city DESC");
# rows = myCursor.fetchall();
# for row in rows:
#     print(row)

# myCursor.execute("""
#     CREATE TABLE payment(
#         customer_id INT PRIMARY KEY,
#         name VARCHAR(50),
#         mode VARCHAR(50),
#         city VARCHAR(50))
# """)

# sql = "INSERT INTO payment (customer_id, name, mode, city) VALUES (%s, %s, %s, %s)";
# values = [
#     (101, 'Olivia Barret', 'Netbanking', 'Portland'),
#     (102, 'Ethan Sinclair', 'Credit Card', 'Miami'),
#     (103, 'Maya Hernandez', 'Credit Cart', 'Seattle'),
#     (104, 'Liam Donovan', 'Netbanking', 'Denver'),
#     (105, 'Sophia Negyuen', 'Credit Card', 'New Orleans'),
#     (106, 'Caleb Foster', 'Debit Card', 'Minneapolis'),
#     (107, 'Ava Patel', 'Debit Card', 'Pheonix'),
#     (108, 'Lucas Carter', 'Netbanking', 'Boston'),
#     (109, 'Isabella Martinez', 'Netbanking', 'Nashville'),
#     (110, 'Jackson Brooks', 'Credit Card', 'Boston')
# ]

# myCursor.executemany(sql, values);

# myCursor.execute("""
#     SELECT mode, COUNT(mode) AS payment_total
#     FROM payment
#     GROUP BY mode
# """);
# rows = myCursor.fetchall();
# for row in rows:
#     print(row)

# myCursor.execute("DROP TABLE payment");

# myCursor.execute("UPDATE student SET grade = 'O' WHERE grade = 'A'");
# mydb.commit();
# myCursor.execute("SELECT * from student");
# rows = myCursor.fetchall();
# for row in rows:
#     print (row)