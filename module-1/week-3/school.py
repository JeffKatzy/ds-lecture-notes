from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text, ForeignKey

from sqlalchemy.orm import sessionmaker, relationship, backref
import sqlalchemy

Base = declarative_base()

class Campus(Base):
    __tablename__ = 'campuses'
    id = Column(Integer, primary_key = True)
    location_name = Column(Text)
    teachers = relationship("Teacher", back_populates="campus")

class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key = True)
    name = Column(Text)
    campus_id = Column(Integer, ForeignKey('campuses.id'))
    campus = relationship(Campus, back_populates="teachers")

engine = sqlalchemy.create_engine('sqlite:///school.db', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
