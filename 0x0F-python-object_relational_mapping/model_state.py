#!/usr/bin/python3
"""Start link class to table in database 
"""


import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Importing Base from SQLAlchemy
Base = declarative_base()

class State(Base):
    """State class"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
