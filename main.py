from fastapi import FastAPI, HTTPException,Depends
from bot.bot import NotionBot
from services.parser import *
from sqlalchemy.orm import Session

from database import crud, models, schemas
from database.database import SessionLocal, engine
models.Base.metadata.create_all(bind=engine)


app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/group/init")
async def add_group(url:str = None,db: Session = Depends(get_db)):
    if url is None:
        return HTTPException(status_code=404, detail="Url is None")
    id = get_id_from_url(url)
    init_parse_group(id,db)
    return {"message" : "완료"}
    


@app.get("/submit")
async def post_submit():
    pass