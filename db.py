from sqlalchemy.orm import declarative_base, create_session, sessionmaker, scoped_session
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()


Base = declarative_base()

engine = create_engine(os.environ.get('URL'))

Session = sessionmaker(bind=engine)
session = scoped_session(Session)
