import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    email = Column(String(20), nullable=False, unique=True)
    firstname = Column(String(20), nullable=False)
    lastname = Column(String(250), nullable=False)
    password = Column(String(50), nullable=False)
    username = Column(String(20), nullable=False, unique=True)
    suscriptionDate = Column(String(50), nullable=False)
    
    favorites = relationship('Favorites', backref='user')

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    characters_id = Column(Integer, ForeignKey('characters.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'))

    usuario = relationship('Usuario', backref='favorites') 
    characters = relationship('Characters', backref='favorites')
    planets = relationship('Planets', backref='favorites')
    vehicles = relationship('Vehicles', backref='favorites')

# Generar el diagrama
render_er(Base, 'diagram.png')
