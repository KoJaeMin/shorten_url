from pydantic import BaseModel

class ResponseUrlDto(BaseModel):
  short_url: str