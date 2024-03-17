#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
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

    # Execute a query to select cities with their corresponding state names
    query = "SELECT cities.id, cities.name, states.name FROM cities JOIN states
    ON cities.state_id = states.id ORDER BY cities.id ASC;"
    
    cursor.execute(query)
    
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()
