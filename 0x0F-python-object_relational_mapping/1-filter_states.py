#!/usr/bin/python3
"""
Script that lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa
"""


import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306,
            user=username, passwd=password, db=db_name)
    cursor = db.cursor()
    
    # Execute a query to select states starting with 'N'
    # and order by 'id' in ascending order
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;")
    
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()