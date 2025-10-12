from fastapi import FastAPI
from routes import healthcheck

app = FastAPI()

app.include_router(healthcheck.router)

