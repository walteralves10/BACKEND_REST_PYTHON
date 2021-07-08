from fastapi import FastAPI
from route.messageRoute import message

app = FastAPI()

app.include_router(message)