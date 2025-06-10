import mysql.connector as MyConn

mydb = None
db_cursor = None
try:
    mydb = MyConn.connect(host="localhost", user='root',
                          password="vidhi@2004", database='employee')
    # db_cursor.execute("create database employee")

    db_cursor = mydb.cursor()
    db_cursor.execute("SHOW TABLES")
    for data in db_cursor:
        print(data)

    db_cursor.execute("DROP TABLE IF EXISTS employee")
    create_table_script = ''' CREATE TABLE IF NOT EXISTS employee(
                            id INT PRIMARY KEY,
                            name VARCHAR(40) NOT NULL,
                            salary INT,
                            phone_number BIGINT
                            );'''

    db_cursor.execute(create_table_script)

    insert_query = '''INSERT INTO employee (id ,name,salary,phone_number) Values (%s,%s,%s,%s)'''
    values = [(1, 'xyz', 20000, 56427659126), (2, 'abc', 40000, 52638428126),
              (3, 'qwerty', 30000, 5267647869126), (4, 'gfsaf', 50000, 52686439126)]

    db_cursor.executemany(insert_query, values)
    mydb.commit()
    db_cursor.execute('SELECT * FROM employee')
    result = db_cursor.fetchall()
    print(result)

    update_query = 'UPDATE employee SET Name=%s WHERE id=%s'
    update_value = ('abcd', 2)
    db_cursor.execute(update_query, update_value)

    db_cursor.execute('SELECT * FROM employee')
    for db_data in db_cursor.fetchall():
        print(db_data)

    delete_query = 'DELETE FROM employee WHERE Name=%s'
    delete_value = ('xyz',)
    db_cursor.execute(delete_query, delete_value)
    mydb.commit()
    print(db_cursor.rowcount, "Row deleted")
    db_cursor.execute('SELECT * FROM employee')
    for db in db_cursor.fetchall():
        print(db)

except Exception as error:
    print(error)
"""finally :
    if mydb is not None:
        mydb.close()
    if db_cursor is not None:
        db_cursor.close() """
