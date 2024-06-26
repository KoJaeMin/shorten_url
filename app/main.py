from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from shorten.controller import shortenController
from database import Base, engine

Base.metadata.create_all(bind=engine)

origins = [
  '*'
]

app = FastAPI(
  title="shorten_url API",
  description="API description of shorten_url",
  version="0.0.1",
)

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

app.include_router(shortenController)