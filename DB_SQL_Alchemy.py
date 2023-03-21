from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass
from sqlalchemy_serializer import SerializerMixin


db=SQLAlchemy()


@dataclass
class Games(db.Model,SerializerMixin):
    id_game:int
    name:str
    count_people:str
    time_game:str
    __tablename__ = 'games'
    id_game = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255),nullable=True)
    count_people = db.Column(db.String(20))    
    time_game = db.Column(db.String(10))
    price:int = db.Column(db.Integer)
    icon:str = db.Column(db.String)
    id_game_group:str =db.Column(db.String)

    # def as_dict(self):
    #    return {c.name: getattr(self, c.name) for c in self.__table__.columns}

