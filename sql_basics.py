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

# myCursor.execute("USE COLLEGE");

# myCursor.execute("""
#     CREATE TABLE student(
#         rollno INT PRIMARY KEY,
#         name VARCHAR(50),
#         marks INT NOT NULL,
#         grade VARCHAR(1),
#         city VARCHAR(20))
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

# myCursor.execute("""
#     CREATE TABLE dept(
#         id INT PRIMARY KEY,
#         name VARCHAR(50)
#     )
# """)

# sql = "INSERT INTO dept (id, name) VALUES (%s, %s)";
# values = [
#     (101, 'english'),
#     (102, 'IT')
# ]

# myCursor.executemany(sql, values);

# myCursor.execute("SELECT * from dept");
# tabs = myCursor.fetchall();
# print("Rows fetched:", len(tabs))
# for tab in tabs:
#     print(tab)

# myCursor.execute("""
#     CREATE TABLE teacher(
#         id INT PRIMARY KEY,
#         name VARCHAR(50),
#         dept_id INT,
#         FOREIGN KEY (dept_id) REFERENCES dept(id)
#         ON UPDATE CASCADE
#         ON DELETE CASCADE)
# """)

# sql = "INSERT INTO teacher (id, name, dept_id) VALUES (%s, %s, %s)";
# values = [
#     (101, 'Adam', 101),
#     (102, 'Eve', 102)
# ]

# myCursor.executemany(sql, values);
# myCursor.execute("SELECT * from teacher");
# tabs = myCursor.fetchall();
# print("Rows fetched:", len(tabs))
# for tab in tabs:
#     print(tab)

# myCursor.execute("DROP DATABASE IF EXISTS college");













# myCursor.execute("CREATE DATABASE college");
# myCursor.execute("USE college");
# mydb.commit();

# myCursor.execute("""
#     CREATE TABLE student(
#         rollno INT PRIMARY KEY,
#         name VARCHAR(50),
#         marks INT NOT NULL,
#         grade VARCHAR(1),
#         city VARCHAR(20))
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

# myCursor.executemany(sql, values);


# myCursor.execute("SELECT * from student");
# rows = myCursor.fetchall();
# print("Rows fetched:", len(rows));
# for row in rows:
#     print(row)


# myCursor.execute("DROP DATAbASE IF ExISTS college");













# myCursor.execute("CREATE DATABASE school");
# myCursor.execute("USE school");

# myCursor.execute("""
#     CREATE TABLE students(
#         id INT PRIMARY KEY,
#         name VARCHAR(50),
#         age INT
#     )
# """)

# myCursor.execute("""
#     CREATE TABLE classes(
#         id INT PRIMARY KEY,
#         name VARCHAR(50)
#     )
# """)

# myCursor.execute("""
#     CREATE TABLE enrollments(
#         id INT PRIMARY KEY,
#         student_id INT,
#         class_id INT,
#         FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
#         FOREIGN KEY (class_id) REFERENCES classes(id) ON DELETE CASCADE)
# """)

# myCursor.execute("""
#     CREATE TABLE marks(
#         id INT PRIMARY KEY,
#         student_id INT,
#         class_id INT,
#         score INT,
#         FOREIGN KEY (student_id) REFERENCES students(id),
#         FOREIGN KEY (class_id) REFERENCES classes(id)
#     )
# """)

# mydb.commit();
# print("Database and tables created successfully!")

# students = [
#     (1, 'Shruti', 22),
#     (2, 'Abhishek', 19),
#     (3, 'Aditi', 21)
# ]

# classes = [
#     (1, 'Math'),
#     (2, 'Science')
# ]

# enrollments = [
#     (1, 1, 1),
#     (2, 2, 1),
#     (3, 3, 2)
# ]

# myCursor.executemany("INSERT INTO students VALUES(%s, %s, %s)", students);
# myCursor.executemany("INSERT INTO classes VALUES (%s, %s)", classes);
# myCursor.executemany("INSERT INTO enrollments VALUES(%s, %s, %s)", enrollments);
# mydb.commit();

# print("Enrollments BEFORE deleting Shruti: ")
# myCursor.execute("SELECT * FROM enrollments");
# for rows in myCursor.fetchall():
#     print(rows)

# myCursor.execute("DELETE FROM students WHERE id = 1")
# mydb.commit();

# print("Enrollments AFTER deleting Shruti: ")
# myCursor.execute("SELECT * FROM enrollments");
# for row in myCursor.fetchall():
#     print(row)

# myCursor.execute("DROP TABLE IF EXISTS enrollments");
# myCursor.execute("DROP TABLE IF EXISTS marks");
# myCursor.execute("DROP TABLE IF EXISTS students");
# myCursor.execute("DROP TABLE IF EXISTS classes");
# mydb.commit();

# Create fresh tables
# myCursor.execute("""
#     CREATE TABLE students (
#         id INT PRIMARY KEY,
#         name VARCHAR(50),
#         age INT
#     )
# """)

# myCursor.execute("""
#     CREATE TABLE classes (
#         id INT PRIMARY KEY,
#         name VARCHAR(50)
#     )
# """)

# myCursor.execute("""
#     CREATE TABLE enrollments (
#         id INT PRIMARY KEY,
#         student_id INT,
#         class_id INT,
#         FOREIGN KEY (student_id) REFERENCES students(id)
#             ON DELETE CASCADE
#             ON UPDATE CASCADE,
#         FOREIGN KEY (class_id) REFERENCES classes(id)
#             ON DELETE CASCADE
#             ON UPDATE CASCADE
#     )
# """)
# mydb.commit()

# students = [
#     (1, 'Shruti', 21),
#     (2, 'Abhishek', 22),
#     (3, 'Aditi', 20)
# ]
# classes = [
#     (1, 'Math'),
#     (2, 'Science')
# ]
# enrollments = [
#     (1, 1, 1),  # Shruti in Math
#     (2, 2, 1),  # Abhishek in Math
#     (3, 3, 2)   # Aditi in Science
# ]

# myCursor.executemany("INSERT INTO students VALUES (%s, %s, %s)", students)
# myCursor.executemany("INSERT INTO classes VALUES (%s, %s)", classes)
# myCursor.executemany("INSERT INTO enrollments VALUES (%s, %s, %s)", enrollments)
# mydb.commit()

# print("Enrollments BEFORE updating Shruti's ID: ")
# myCursor.execute("SELECT * from enrollments")
# for row in myCursor.fetchall():
#     print(row)

# myCursor.execute("UPDATE students SET id = 11 WHERE id = 1")
# mydb.commit();

# print("Enrollments AFTER updating Shruti's ID: ")
# myCursor.execute("SELECT * from enrollments")
# for row in myCursor.fetchall():
#     print(row)

# myCursor.execute("ALTER TABLE students ADD email VARCHAR(100)")
# mydb.commit();

# myCursor.execute("ALTER TABLE students MODIFY name VARCHAR(100)")
# mydb.commit();

# myCursor.execute("ALTER TABLE students CHANGE age student_age TINYINT")
# mydb.commit();

# myCursor.execute("ALTER TABLE pupils DROP COLUMN email")
# mydb.commit();

# myCursor.execute("RENAME TABLE students TO pupils")
# mydb.commit();

# myCursor.execute("DESCRIBE pupils")
# for col in myCursor.fetchall():
#     print(col)

# print("Before truncate:")
# myCursor.execute("SELECT * from pupils")
# for tab in myCursor.fetchall():
#     print(tab)

# myCursor.execute("DELETE FROM pupils")
# mydb.commit();

# myCursor.execute("SELECT * FROM pupils")
# rows = myCursor.fetchall()
# print("🧹 After truncate:")
# for row in rows:
#     print(row)

# myCursor.execute("DROP TABLE IF EXISTS enrollments")
# myCursor.execute("DROP TABLE IF EXISTS classes")
# myCursor.execute("DROP TABLE IF EXISTS students")

# myCursor.execute("""
#     CREATE TABLE students (
#         id INT PRIMARY KEY,
#         name VARCHAR(50),
#         age INT
#     )
# """)

# myCursor.execute("""
#     CREATE TABLE classes (
#         id INT PRIMARY KEY,
#         name VARCHAR(50)
#     )
# """)

# myCursor.execute("""
#     CREATE TABLE enrollments (
#         id INT PRIMARY KEY,
#         student_id INT,
#         class_id INT,
#         FOREIGN KEY (student_id) REFERENCES students(id)
#             ON DELETE CASCADE
#             ON UPDATE CASCADE,
#         FOREIGN KEY (class_id) REFERENCES classes(id)
#             ON DELETE CASCADE
#             ON UPDATE CASCADE
#     )
# """)

# myCursor.execute("RENAME TABLE pupils TO students")
# mydb.commit()

# students = [
#     (1, 'Shruti', 21),
#     (2, 'Abhishek', 22),
#     (3, 'Aditi', 20)
# ]
# classes = [
#     (1, 'Math'),
#     (2, 'Science'),
#     (3, 'History')
# ]
# enrollments = [
#     (1, 1, 1),  # Shruti in Math
#     (2, 2, 1),  # Abhishek in Math
#     (3, 3, 2)   # Aditi in Science
# ]

# myCursor.executemany("INSERT INTO pupils VALUES (%s, %s, %s)", students)
# myCursor.executemany("INSERT INTO classes VALUES (%s, %s)", classes)
# myCursor.executemany("INSERT INTO enrollments VALUES (%s, %s, %s)", enrollments)
# mydb.commit()

# myCursor.execute("DROP DATABASE IF EXISTS school")

# myCursor.execute("CREATE DATABASE project_hub")
myCursor.execute("USE project_hub")

# myCursor.execute("""
# CREATE TABLE departments (
#     id INT PRIMARY KEY,
#     name VARCHAR(50)
# )
# """)

# myCursor.execute("""
# CREATE TABLE employees (
#     id INT PRIMARY KEY,
#     name VARCHAR(50),
#     department_id INT,
#     salary INT,
#     FOREIGN KEY (department_id) REFERENCES departments(id)
# )
# """)

# myCursor.execute("""
# CREATE TABLE projects (
#     id INT PRIMARY KEY,
#     title VARCHAR(100),
#     employee_id INT,
#     FOREIGN KEY (employee_id) REFERENCES employees(id)
# )
# """)

# myCursor.execute("""
# CREATE TABLE salaries (
#     id INT PRIMARY KEY,
#     employee_id INT,
#     amount INT,
#     bonus INT,
#     FOREIGN KEY (employee_id) REFERENCES employees(id)
# )
# """)

# mydb.commit()
# print("✅ Clean tables created successfully.")

# Departments
# departments = [
#     (1, 'Engineering'),
#     (2, 'Marketing'),
#     (3, 'HR')
# ]
# myCursor.executemany("INSERT INTO departments VALUES (%s, %s)", departments)

# Employees
# employees = [
#     (101, 'Shruti', 1, 70000),
#     (102, 'Abhishek', 1, 65000),
#     (103, 'Aditi', 2, 50000),
#     (104, 'Rahul', 3, 40000),
#     (105, 'Esha', 2, 55000)
# ]
# myCursor.executemany("INSERT INTO employees VALUES (%s, %s, %s, %s)", employees)

# # Projects
# projects = [
#     (201, 'Website Redesign', 101),
#     (202, 'Ad Campaign', 103),
#     (203, 'Recruitment Drive', 104),
#     (204, 'Backend API', 102),
#     (205, 'SEO Optimization', 105)
# ]
# myCursor.executemany("INSERT INTO projects VALUES (%s, %s, %s)", projects)

# # Salaries
# salaries = [
#     (301, 101, 70000, 5000),
#     (302, 102, 65000, 4000),
#     (303, 103, 50000, 3000),
#     (304, 104, 40000, 2000),
#     (305, 105, 55000, 3500)
# ]
# myCursor.executemany("INSERT INTO salaries VALUES (%s, %s, %s, %s)", salaries)

# mydb.commit()
# print("📊 Sample data inserted successfully!")

# sql = """
#     SELECT employees.name as employee_name, departments.name as department_name
#     FROM employees
#     INNER JOIN departments
#     ON employees.department_id = departments.id    
# """
# myCursor.execute(sql)
# results = myCursor.fetchall();
# print("🧾 Employees and their Departments (INNER JOIN):")
# for row in results:
#     print(row)

# myCursor.execute("INSERT INTO employees (id, name, department_id, salary) VALUES (106, 'Nikhil', NULL, 48000)")
# mydb.commit()

# sql = """
#     SELECT employees.name AS employee_name, departments.name AS department_name
#     FROM employees
#     LEFT JOIN departments
#     ON employees.department_id = departments.id
# """
# myCursor.execute(sql)
# results = myCursor.fetchall()
# print("👥 All employees (LEFT JOIN):")
# for row in results:
#     print(row)

# sql = """
#     SELECT name FROM employees
#     UNION
#     SELECT employees.name FROM projects
#     INNER JOIN employees ON projects.employee_id = employees.id
# """
# myCursor.execute(sql)
# results = myCursor.fetchall()
# print("🧑‍💻 Unique names of all employees & project leads:")
# for row in results:
#     print(row[0])

# sql = """
#     SELECT name, salary
#     FROM employees
#     WHERE salary > (
#         SELECT AVG(salary) FROM employees
#     )
# """
# myCursor.execute(sql)
# rows = myCursor.fetchall()
# print("💸 Employees earning more than average salary:")
# for row in rows:
#     print(row)

# sql = """
#     SELECT title 
#     FROM projects
#     WHERE employee_id = (
#         SELECT id FROM employees
#         ORDER BY salary DESC
#         LIMIT 1
#     )
# """
# myCursor.execute(sql)
# rows = myCursor.fetchall()
# print("🏆 Project of highest paid employee:")
# for row in rows:
#     print(row[0])

# sql = """
#     SELECT name, 
#     (
#         SELECT bonus
#         FROM salaries
#         WHERE salaries.employee_id = employees.id
#     ) AS bonus
#     FROM employees
# """
# myCursor.execute(sql)
# rows = myCursor.fetchall()
# print("🎁 Employees and their bonuses:")
# for row in rows:
#     print(row)


# myCursor.execute("""
#     CREATE VIEW high_earners AS
#     SELECT name, salary FROM employees
#     WHERE salary > 60000
# """)
# mydb.commit();
# myCursor.execute("SELECT * FROM high_earners")
# for row in myCursor.fetchall():
#     print(row)


# myCursor.execute("DROP VIEW IF EXISTS high_earners")