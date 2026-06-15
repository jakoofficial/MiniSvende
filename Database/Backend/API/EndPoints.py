from fastapi import Depends, FastAPI
from ..DBConn import *
from sqlalchemy.orm import Session

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/getItem")
def read_item(db: Session = Depends(get_db)):
    testobj = db.query(test).first()
    return testobj.name