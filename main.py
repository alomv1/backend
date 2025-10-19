from fastapi import FastAPI
from routes import healthcheck, user

app = FastAPI()

app.include_router(healthcheck.router)
app.include_router(user.router)
