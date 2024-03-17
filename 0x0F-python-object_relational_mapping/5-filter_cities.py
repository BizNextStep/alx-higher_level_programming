#!/usr/bin/python3
"""
Script that lists all cities of a given state from the database hbtn_0e_4_usa
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

    # Execute a query to select cities of the given state
    query = "SELECT GROUP_CONCAT(name SEPARATOR ', ') FROM cities
    JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id ASC;"
    
    cursor.execute(query, (state_name,))
    
    results = cursor.fetchall()

    for row in results:
        print(row[0])

    cursor.close()
    db.close()
