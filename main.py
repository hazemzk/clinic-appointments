from fastapi import FastAPI
import models
import database
from routers import patients, appointments

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(patients.router)
app.include_router(appointments.router)
