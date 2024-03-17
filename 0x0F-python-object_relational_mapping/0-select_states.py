#!/usr/bin/python3
import MySQLdb
import sys


def select_states(username, password, db_name):
    # Connect to the MySQL server
    db = MySQLdb.connect(host='localhost', port=3306, user=username,
            passwd=password, db=db_name)

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query to retrieve all states sorted by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows
    rows = cursor.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Extract username, password, and database name from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Call the function to select states
    select_states(username, password, db_name)
