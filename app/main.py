from fastapi import FastAPI
from app.routes.authroutes import authrouter
from app.routes.taskroutes import todorouter

app = FastAPI()

app.include_router(todorouter)
app.include_router(authrouter)