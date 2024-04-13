import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class user(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)


class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    birth_year = Column(String(250))
    eye_color = Column(String(250))
    films = Column(String(250))  
    gender = Column(String(250))
    hair_color = Column(String(250))
    height = Column(String(250))
    homeworld = Column(Integer, ForeignKey('planets.id'))
    planets = relationship('Planets')
    mass = Column(String(250))
    name = Column(String(250))
    skin_color = Column(String(250))
    created = Column(String(250))
    edited = Column(String(250))
    species = Column(String(250))  
    starships = Column(String(250))  
    url = Column(String(250))
    vehicles = Column(String(250))
    

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    climate = Column(String(250))
    created = Column(String(250))
    diameter = Column(String(250))
    edited = Column(String(250))
    films = Column(String(250))  
    gravity = Column(String(250))
    name = Column(String(250))
    orbital_period = Column(String(250))
    population = Column(String(250))
    residents = Column(String(250))  
    rotation_period = Column(String(250))
    surface_water = Column(String(250))
    terrain = Column(String(250))
    url = Column(String(250))

class FavoritesPeople(Base):
    __tablename__ = 'favoritespeople'
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    liked_people = Column(Integer, ForeignKey('people.id'))
    people = relationship('People')
    
class FavoritesPlanets(Base):
    __tablename__ = 'favoritesplanets'
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    liked_planet = Column(Integer, ForeignKey('planets.id'))
    planets = relationship('Planets')

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
