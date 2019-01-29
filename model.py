from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Write your classes here :
class Place(Base):
	__tablename__ = "places"
	id = Column(Integer, primary_key=True)
	name = Column(String)
	info=Column(String)
	photo1=Column(String)
	photo2=Column(String)
	photo3=Column(String)
	link=Column(String)
