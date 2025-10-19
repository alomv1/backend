from fastapi import FastAPI
from routes import healthcheck, user, category, record

app = FastAPI()

app.include_router(healthcheck.router)
app.include_router(user.router)
app.include_router(category.router)
app.include_router(record.router)