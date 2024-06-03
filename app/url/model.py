from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Url(Base):
  __tablename__ = "url"
  
  url = Column(String, primary_key=True)
  hashedKey = Column(String, unique=True)
  