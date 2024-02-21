#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from models.place import Place
from models.review import Review


class User(BaseModel, Base):
    """This is the attributes for user

    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
