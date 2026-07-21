from fastapi import FastAPI


from app.core.database import Base, engine
from app.domains.auth import models

Base.metadata.create_all(bind=engine)


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
