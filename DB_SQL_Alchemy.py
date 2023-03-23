
from sqlalchemy import Column, String
from flask_sqlalchemy import SQLAlchemy,model

# from dataclasses import dataclass
# from sqlalchemy_serializer import SerializerMixin


db = SQLAlchemy()

# @dataclass
class Games(db.Model): #,SerializerMixin):
    __tablename__ = 'games'
    # id_game varchar NOT NULL,
    id_game = db.Column(db.Integer, primary_key=True)
	# id_game_group varchar NOT NULL,
    id_game_group =db.Column(db.String)
    href_img = db.Column(db.String)

	# name_game varchar NULL,
    name_game = db.Column(db.String,nullable=True)
    name_game_ext = db.Column(db.String)
	# count_people varchar NULL,
    count_people = db.Column(db.String(20))    
	# time_game interval NULL,
    time_game = db.Column(db.String(10))
	# lang varchar NULL,
    lang = db.Column(db.String)
	# price numeric NULL,
    price = db.Column(db.Integer)
	# status varchar NULL,
    status = db.Column(db.String)
	# available bool NULL
    available= db.Column(db.Boolean)


    # def as_dict(self):
    #    return {c.name: getattr(self, c.name) for c in self.__table__.columns}

