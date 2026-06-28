from fastapi import FastAPI
from app.routes.authroutes import authrouter

app = FastAPI()

app.include_router(authrouter)