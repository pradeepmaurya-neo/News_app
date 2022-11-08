from db import Base, session, engine
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class Admin(Base):
    __tablename__ = 'admin'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(50))
    # username = Column('username', String(50))
    # password = Column('password', String(150))
    
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
    

Base.metadata.create_all(engine)