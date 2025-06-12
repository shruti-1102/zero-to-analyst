import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Parihar_2003"
)

myCursor = mydb.cursor();

# myCursor.execute("CREATE DATABASE college");

myCursor.execute("USE college");

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

