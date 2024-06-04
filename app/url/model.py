from sqlalchemy import Column, String
from database import Base

class Url(Base):
  __tablename__ = "url"
  
  url = Column(String, primary_key=True)
  hashedKey = Column(String, unique=True)
  