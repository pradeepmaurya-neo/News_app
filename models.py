from db import Base, session, engine
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship

class Admin(Base):
    __tablename__ = 'admin'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(50))    
    user = relationship('User', back_populates='admins')


class User(Base):
    __tablename__ = 'users'

    id = Column('id', Integer, primary_key=True)
    admin_id = Column(ForeignKey('admin.id'))
    name = Column('name', String(50))
    email = Column('email', String(50))
    phone = Column('phone', String(13))
    username = Column('username', String(50))
    password = Column('password', String(150))
    admins = relationship('Admin', back_populates='user')
    posts = relationship('Post', back_populates='users')
    

class Post(Base):
    __tablename__ = "post"
    id = Column('id', Integer,primary_key=True)
    user_id = Column(ForeignKey('users.id'))
    title = Column(String(200))
    publish = Column(Boolean, default=False)
    reviewed = Column(Boolean, default=False)
    top_review = Column(Boolean, default=False)
    conetent = Column(Text)
    users = relationship('User', back_populates='posts')


Base.metadata.create_all(engine)