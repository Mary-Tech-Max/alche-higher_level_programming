#!/usr/bin/python3
"""Module that defines the State class for SQLAlchemy.

This module links the State class to the MySQL table `states` and
exposes the declarative Base used to create that table.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represents a US state stored in the `states` MySQL table.

    Attributes:
        id: an auto-generated, unique integer, primary key.
        name: the name of the state, a string of at most 128
            characters, that cannot be null.
    """
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)
