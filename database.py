from model import *
import wikipedia

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///places.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def create_place(name):
	info= wikipedia.summary(name, sentences=3)
	p = wikipedia.page(name)
	photo1=  p.images[0]
	photo2= p.images[5]
	photo3= p.images[7]
	link= p.url
	place_object = Place(name=name, info=info, photo1=photo1, photo2=photo2, photo3=photo3, link=link)
	session.add(place_object)
	session.commit()

def get_place_by_name(name):
	place=session.query(Place).filter_by(name=name).first()
	return place

def get_all_places():
	places = session.query(Place).all()
	return places

def exist(place):
	places=get_all_places()
	for place in places:
		if place.name==place:
			return True
	return False

create_place("London")
p=get_place_by_name("London")