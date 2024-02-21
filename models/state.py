#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import models
from models.city import City
from models.base_model import BaseModel, Base
import shlex


class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    citie = relationship("City", cascade="all, delete, delete-orphan",
            backref='state')

    @property
    def citie(self):
        var = models.storage.all()

        lista = []

        resuls = []

        for city in var:
            city = city.replace(".", " ")
            city = shlex.split(city)
            if (city[0] == "City"):
                lista.append(var[key])
        for element in lista:
            if (element.id == self.id):
                results.append(element)
        return (results)
