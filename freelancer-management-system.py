import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Parihar_2003'
)

myCursor = mydb.cursor();

# myCursor.execute("CREATE DATABASE freelancer_project")
# mydb.commit();
# myCursor.execute("USE freelancer_project")

# myCursor.execute("""
#     CREATE TABLE freelancers(
#         id INT PRIMARY KEY,
#         name VARCHAR(50),
#         skill VARCHAR(50),
#         experience_yrs INT
#     )
# """)

# free_values = [
#     (1, 'Shruti', 'Web Development', 3),
#     (2, 'Abhishek', 'Graphic Design', 2),
#     (3, 'Aditi', 'Data Analysis', 1),
#     (4, 'Karan', 'App Development', 4)
# ]

# myCursor.executemany("INSERT INTO freelancers VALUES(%s, %s, %s, %s)", free_values)


# myCursor.execute("""
#     CREATE TABLE clients(
#         id INT PRIMARY KEY,
#         name VARCHAR(50),
#         company VARCHAR(50)
#     )
# """)

# client_val = [
#     (1, 'Zara Khan', 'TechNova'),
#     (2, 'Rohan Malhotra', 'MarketEdge'),
#     (3, 'Tina Dey', 'DataWiz')

# ]

# myCursor.executemany("INSERT INTO clients VALUES(%s, %s, %s)", client_val)


# myCursor.execute("""
#     CREATE TABLE projects(
#         id INT PRIMARY KEY,
#         title VARCHAR(100),
#         freelancer_id INT,
#         client_id INT,
#         deadline DATE,
#         FOREIGN KEY (freelancer_id) REFERENCES freelancers(id),
#         FOREIGN KEY (client_id) REFERENCES clients(id)
#     )
# """)

# project_val = [
#     (1, 'Website Revamp', 1, 1, '2025-08-15'),
#     (2, 'App UI Redesign', 2, 2, '2025-07-20'),
#     (3, 'Customer Insights', 3, 3, '2025-09-01'),
#     (4, 'Inventory App', 4, 1, '2025-06-30'),
#     (5, 'Dashboard Upgrade', 1, 3, '2025-10-10')
# ]

# myCursor.executemany("INSERT INTO projects VALUES (%s, %s, %s, %s, %s)", project_val)


# myCursor.execute("""
#     CREATE TABLE payments(
#         id INT PRIMARY KEY,
#         project_id INT,
#         amount INT,
#         status VARCHAR(20),
#         bonus INT,
#         FOREIGN KEY (project_id) REFERENCES projects(id)
#     )
# """)

# payments_val = [
#     (1, 1, 35000, 'Paid', 5000),
#     (2, 2, 20000, 'Pending', 0),
#     (3, 3, 25000, 'Paid', 2000),
#     (4, 4, 40000, 'Paid', 3000),
#     (5, 5, 28000, 'Pending', 0)
# ]

# myCursor.executemany("INSERT INTO payments VALUES(%s, %s, %s, %s, %s)", payments_val)


# myCursor.execute("DROP DATABASE IF EXISTS freelancer_project")






# myCursor.execute("CREATE DATABASE freelancer_project")
myCursor.execute("USE freelancer_project")

# myCursor.execute("""
# CREATE TABLE freelancers (
#     id INT PRIMARY KEY,
#     name VARCHAR(50),
#     skill VARCHAR(50),
#     experience_yrs INT
# )
# """)

# myCursor.execute("""
# CREATE TABLE clients (
#     id INT PRIMARY KEY,
#     name VARCHAR(50),
#     company VARCHAR(50)
# )
# """)

# myCursor.execute("""
# CREATE TABLE projects (
#     id INT PRIMARY KEY,
#     title VARCHAR(100),
#     freelancer_id INT,
#     client_id INT,
#     deadline DATE,
#     FOREIGN KEY (freelancer_id) REFERENCES freelancers(id),
#     FOREIGN KEY (client_id) REFERENCES clients(id)
# )
# """)

# myCursor.execute("""
# CREATE TABLE payments (
#     id INT PRIMARY KEY,
#     project_id INT,
#     amount INT,
#     status VARCHAR(20),
#     bonus INT,
#     FOREIGN KEY (project_id) REFERENCES projects(id)
# )
# """)

# mydb.commit()
# print("🎉 Tables created successfully!")

# freelancers = [
#     (1, 'Shruti', 'Web Development', 3),
#     (2, 'Abhishek', 'Graphic Design', 2),
#     (3, 'Aditi', 'Data Analysis', 1),
#     (4, 'Karan', 'App Development', 4)
# ]
# myCursor.executemany("INSERT INTO freelancers VALUES (%s, %s, %s, %s)", freelancers)

# clients = [
#     (1, 'Zara Khan', 'TechNova'),
#     (2, 'Rohan Malhotra', 'MarketEdge'),
#     (3, 'Tina Dey', 'DataWiz')
# ]
# myCursor.executemany("INSERT INTO clients VALUES (%s, %s, %s)", clients)

# projects = [
#     (1, 'Website Revamp', 1, 1, '2025-08-15'),
#     (2, 'App UI Redesign', 2, 2, '2025-07-20'),
#     (3, 'Customer Insights', 3, 3, '2025-09-01'),
#     (4, 'Inventory App', 4, 1, '2025-06-30'),
#     (5, 'Dashboard Upgrade', 1, 3, '2025-10-10')
# ]
# myCursor.executemany("INSERT INTO projects VALUES (%s, %s, %s, %s, %s)", projects)

# payments = [
#     (1, 1, 35000, 'Paid', 5000),
#     (2, 2, 20000, 'Pending', 0),
#     (3, 3, 25000, 'Paid', 2000),
#     (4, 4, 40000, 'Paid', 3000),
#     (5, 5, 28000, 'Pending', 0)
# ]
# myCursor.executemany("INSERT INTO payments VALUES (%s, %s, %s, %s, %s)", payments)

# mydb.commit()
# print("✅ Sample data inserted!")


sql = """
    SELECT projects.title, clients.name AS name, clients.company, payments.status
    FROM projects
    JOIN clients ON projects.client_id = clients.id
    JOIN payments ON projects.id = payments.project_id
    WHERE payments.status = 'Pending'
"""
myCursor.execute(sql)
for tab in myCursor.fetchall():
    print(tab)