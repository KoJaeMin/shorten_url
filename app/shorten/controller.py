from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse
from url import RequestUrlDto, ResponseUrlDto
from shorten.service import ShortenService

shortenController = APIRouter()
service = ShortenService()

@shortenController.get(
  '/{short_key}',
  summary='Redirect Original URL',
  description='Redirect to the original URL using the shortened key'
)
def getUrl(short_key: str):
  url = service.getUrl(short_key)
  if url == '':
    raise HTTPException(404, detail=f"Not found the key {short_key}")
  return RedirectResponse(url=url, status_code=301)

@shortenController.post(
  '/shorten',
  response_model=ResponseUrlDto,
  summary='Create shortened URL',
  description='Transform the received long URL into a unique shortened key and store it in the database'
)
def createShorten(requestUrlDto: RequestUrlDto) -> ResponseUrlDto:
  url = requestUrlDto.url
  
  short_key = service.getUrlKey(url=url)
  
  if short_key == '':
    shortUrl = service.addShortenUrl(url)
  
  responseUrlDto = ResponseUrlDto(short_url=shortUrl) if short_key == '' else ResponseUrlDto(short_url=short_key)

  return responseUrlDto