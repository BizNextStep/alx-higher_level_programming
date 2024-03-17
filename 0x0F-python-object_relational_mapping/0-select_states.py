#!/usr/bin/python3
import MySQLdb
import sys


# Ensure the code is not executed when imported
if __name__ == "__main__":
    # Extract MySQL credentials from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306,
            user=username, passwd=password, db=db_name)
    
    # Create a cursor object to interact with the database
    cursor = db.cursor()
    
    # Execute a query to select all data from the 'states' table
    # and order by 'id' in ascending order
    cursor.execute("SELECT * FROM states ORDER BY id ASC;")
    
    # Fetch all the results from the executed query
    results = cursor.fetchall()

    # Iterate over the results and print each row
    for row in results:
        print(row)

    # Close the cursor to release resources
    cursor.close()
    
    # Close the database connection
    db.close()
