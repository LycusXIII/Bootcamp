'''
This program creates and inserts data into a database as well as
manipulates the date within.
'''
import sqlite3
import os

# Checks if db exists
db_exists = os.path.exists('python_programming.db')
try:
    db = sqlite3.connect('python_programming.db')
    cursor = db.cursor()
    if not db_exists:
        cursor.execute(
            '''CREATE TABLE python_programming(id INTEGER PRIMARY KEY,
            name TEXT, grade INTEGER)''')
        db.commit()
except sqlite3.Error as e:
    print(f"Error creating the database: {e}")
else:
    # Inserts data if db wasn't created before
    if not cursor.execute('''SELECT * FROM python_programming''').fetchone():
        student_info = [
            (55, 'Carl Davis', 61),
            (66, 'Dennis Fredrickson', 88),
            (77, 'Jane Richards', 78),
            (12, 'Peyton Sawyer', 45),
            (2, 'Lucas Brooke', 99)]
        db.commit()
        cursor.executemany('''INSERT INTO python_programming(id, name, grade)
                        VALUES(?,?,?)''', student_info)
        cursor.execute('''SELECT * FROM python_programming
                    WHERE grade BETWEEN 60 AND 80''')
        students = cursor.fetchall()
        print(students)
        id = 55
        grade = 65
        cursor.execute('''UPDATE python_programming SET grade = ?
                       WHERE id = ?''', (grade, id))
        id = 66
        cursor.execute('''DELETE FROM python_programming
                       WHERE id = ? ''', (id,))
        id = 55
        grade = 80
        cursor.execute('''UPDATE python_programming SET grade = ?
                       WHERE id > ?''', (grade, id))
        db.commit()
    db.close()
