from Backend.DBConn import *

from fastapi import Depends, FastAPI, HTTPException
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

@app.get("/getUser")
def read_item(userID: int, db: Session = Depends(get_db)):
    profile = db.query(UserProfile).filter(UserProfile.user_id == userID).first()

    if not profile:
        raise HTTPException(status_code=404, detail="User not found")
    
    return {
        "user_id: ": profile.user_id,
        "username": profile.username
    }

@app.post("/signin")
def user_signin(username, password, db: Session = Depends(get_db)):
    user = db.query(UserProfile).filter(UserProfile.username == username).first()
    if user and user.signin.password == password:
        sess = UserSession()
        sess.session_key = "000001"
        sess.user_id = user.user_id
        db.add(sess)
        db.commit()
        db.refresh(sess)

        u = {"name": user.username}

        return [u, sess]
    
    return "No user found"
    # signin = db.query

    pass