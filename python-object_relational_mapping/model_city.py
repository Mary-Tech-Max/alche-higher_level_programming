#!/usr/bin/python3
"""Module that defines the City class for SQLAlchemy.

This module links the City class to the MySQL table `cities`.
"""
from sqlalchemy import Column, ForeignKey, Integer, String
from model_state import Base


class City(Base):
    """Represents a city stored in the `cities` MySQL table.

    Attributes:
        id: an auto-generated, unique integer, primary key.
        name: the name of the city, a string of at most 128
            characters, that cannot be null.
        state_id: the id of the state this city belongs to, a
            foreign key to states.id, that cannot be null.
    """
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
