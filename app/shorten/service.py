from sqlalchemy.orm import Session
from database import SessionLocal
from url import Url
from hashlib import sha256
from base64 import urlsafe_b64encode

class ShortenService():
  def __init__(self, db: Session = SessionLocal()) -> None:
    self.db = db
    self.length = 8
    
  def getUrlKey(self, url: str) -> str:
    result = self.db.query(Url).filter(Url.url == url).first()
    
    if result is not None:
      return result.hashedKey
    
    return ''
    
  def getUrl(self, key: str) -> str:
    result = self.db.query(Url).filter(Url.hashedKey == key).first()
    
    if result is not None:
      return result.url
    
    return ''

  def addShortenUrl(self, url: str) -> str:    
    hashedKey: str = self.convertShorten(target=url, len=self.length)
    result = self.db.query(Url).filter(Url.hashedKey == hashedKey).first()
    
    while result is not None:
      hashedKey = self.convertShorten(target=hashedKey, len=self.length)
      result = self.db.query(Url).filter(Url.hashedKey == hashedKey).first()
      
    newUrl: Url = Url(url=url, hashedKey=hashedKey)
    self.db.add(newUrl)
    self.db.commit()
    self.db.refresh(newUrl)
    
    return hashedKey
  
  def convertShorten(self, target: str, len: int) -> str:
    sha256_hash: bytes = sha256(target.encode()).digest()
    base64_hash: str = urlsafe_b64encode(sha256_hash).rstrip(b'=').decode('utf-8')
    short_hash: str = base64_hash[:len]
    
    return short_hash