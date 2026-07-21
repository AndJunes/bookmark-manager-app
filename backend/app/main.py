from fastapi import FastAPI


from app.api.router import api_router
from app.core.database import Base, engine
from app.domains.auth import models

Base.metadata.create_all(bind=engine)


app = FastAPI()


app.include_router(api_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
