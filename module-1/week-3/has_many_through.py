from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text, ForeignKey, String

from sqlalchemy.orm import sessionmaker, relationship, backref
import sqlalchemy

Base = declarative_base()

class Artist(Base):
    __tablename__ = 'artists'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    genres = relationship(
        'Genre',
        secondary='songs',
    )

class Genre(Base):
    __tablename__ = 'genres'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    artists = relationship(
        Artist,
        secondary='songs'
    )

class Song(Base):
    __tablename__ = 'songs'
    id = Column(Integer, primary_key=True)
    artist_id = Column(Integer, ForeignKey('artists.id'))
    genre_id = Column(Integer, ForeignKey('genres.id'))
    name = Column(String)
    artist = relationship(Artist, backref=backref("songs"))
    genre = relationship(Genre, backref=backref("songs"))


engine = sqlalchemy.create_engine('sqlite:///playlister.db', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
