#!/usr/bin/python3
"""
Script that displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""


import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
            user=username, passwd=password, db=db_name)
    cursor = db.cursor()

    # Create the SQL query using user input for state name
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC;".format(state_name)
    
    cursor.execute(query)
    
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()
