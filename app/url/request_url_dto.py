from pydantic import BaseModel

class RequestUrlDto(BaseModel):
  url: str