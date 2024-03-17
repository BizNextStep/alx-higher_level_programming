#!/usr/bin/python3
"""Creates the State "California" with the City "San Francisco"
from the database hbtn_0e_100_usa"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Create engine to establish connection to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Create a new State object
    california = State(name="California")

    # Create a new City object
    san_francisco = City(name="San Francisco")

    # Add the new City object to the State object's list of cities
    california.cities.append(san_francisco)

    # Add the State object to the session
    session.add(california)

    # Commit the changes
    session.commit()

    # Close the session
    session.close()
