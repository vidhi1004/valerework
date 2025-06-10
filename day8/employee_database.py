import mysql.connector as conn


mydb = conn.connect(host='localhost', user='root',
                    password='', database='Employee')
db_cursor = mydb.cursor()

# db_cursor.execute("DROP DATABASE IF EXISTS Employee")

# db_cursor.execute("CREATE DATABASE IF NOT EXISTS Employee ")


def create_table():
    # db_cursor.execute("DROP TABLE IF EXISTS employee")
    script_create_table = ''' CREATE TABLE IF NOT EXISTS employee
                    ( id INT PRIMARY KEY,
                    name VARCHAR(255),
                    email VARCHAR(255),
                    salary INT,
                    phone_number BIGINT
                    )'''

    db_cursor.execute(script_create_table)
    mydb.commit()


def add_data():
    empid = input("Enter id :")
    name = input("Enter name:")
    email = input("Enter email:")
    salary = input("Enter salary:")
    phone_number = input("Enter phone_number:")
    insert_value = (empid, name, email, salary, phone_number)
    insert_query = 'INSERT INTO employee (id ,name,email,salary,phone_number) VALUES (%s,%s,%s,%s,%s)'

    db_cursor.execute(insert_query, insert_value)
    mydb.commit()
    print("employee added successfully")


def display_employee():
    display = 'SELECT * FROM employee WHERE id =%s'
    empid = input("Enter the employee id")
    display_data = (empid,)
    db_cursor.execute(display, display_data)

    for data in db_cursor.fetchall():
        print(data)
    mydb.commit()


def display_all_employees():
    display = 'SELECT * FROM employee'
    db_cursor.execute(display)
    for data in db_cursor.fetchall():
        print(data)

    mydb.commit()


def update_details():
    name = input("Enter the column in which you want to make change:")
    value1 = input("Enter the value you want to set:")
    eid = int(input("Enter the employee id to make changes:"))
    if name == 'salary' or name == 'phone_number':
        update_query = (f"UPDATE employee SET {name}={value1} WHERE id={eid}")
    else:
        update_query = (
            f"UPDATE employee SET {name}='{value1}' WHERE id={eid}")
    db_cursor.execute(update_query)
    mydb.commit()
    print("Updated successfully")


def delete_details():
    value = int(input("Enter the id:"))
    delete = 'DELETE FROM employee WHERE id=%s'
    delete_value = (value,)
    db_cursor.execute(delete, delete_value)
    display_all_employees()
    mydb.commit()


def delete_all():
    db_cursor.execute("TRUNCATE TABLE employee")
    print("empty")
    mydb.commit()


while True:
    key = int(input("Enter the key specific to the task you want to perform :\n"
                    "1)Add Data\n"
                    "2)Update details\n"
                    "3)Display Employee\n"
                    "4)Display All Employees\n"
                    "5)Delete Employee\n"
                    "6)Delete ALL Employees\n"
                    "7)Exit"))
    if key == 1:
        create_table()
        add_data()
    elif key == 2:
        update_details()
    elif key == 3:
        display_employee()
    elif key == 4:
        display_all_employees()
    elif key == 5:
        delete_details()
    elif key == 6:
        delete_all()
    elif key == 7:
        break
    else:
        print("Wrong key entered")
