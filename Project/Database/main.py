from Backend.DBConn import *

from fastapi.middleware.cors import CORSMiddleware
from fastapi import Depends, FastAPI, HTTPException, Body, Header
from sqlalchemy.orm import Session

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/getUser")
def read_item(userID: int = Header(), db: Session = Depends(get_db)):
    profile = db.query(UserProfile).filter(UserProfile.user_id == userID).first()

    if not profile:
        raise HTTPException(status_code=404, detail="User not found")
    
    return {
        "user_id: ": profile.user_id,
        "username": profile.username
    }

@app.get("/getUserBySession")
def get_user_by_session(session_token:str = Header(), db: Session = Depends(get_db)):
    session = db.query(UserSession).filter(UserSession.session_key == session_token).first()
    if not session:
        raise HTTPException(status_code=404, detail="No session found")

    user = db.query(UserProfile).filter(UserProfile.user_id == session.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="No user found")
    
    sub = db.query(Subscriptions).filter(Subscriptions.user_id == user.user_id).first()
    if not sub:
        raise HTTPException(status_code=404, detail="No one found")

    return {
        "username" : user.username,
        "sub" : sub.subscription,
    }

@app.post("/createUser")
def create_user(username:str = Body(), password:str = Body(), db: Session = Depends(get_db)):
    qUser = db.query(UserProfile).filter(UserProfile.username == username).first()
    if qUser: return "Username already exists"

    signin = UserSignin()
    signin.password = password
    db.add(signin)
    db.commit()
    db.refresh(signin)
    
    if signin:
        user = UserProfile()
        user.username = username
        user.signin_id = signin.signin_id
        db.add(user)
        db.commit()
        db.refresh(user)

        sub = Subscriptions()
        sub.user_id = user.user_id
        db.add(sub)
        db.commit()
        
        if user:
            return "User created"
    return "Something went wrong. Try again"

@app.post("/signin")
def user_signin(username:str = Body(), password:str = Body(), db: Session = Depends(get_db)):
    user = db.query(UserProfile).filter(UserProfile.username == username).first()
    if user and user.signin.password == password:
        sess = UserSession()
        sess.user_id = user.user_id
        db.add(sess)
        db.commit()
        db.refresh(sess)

        u = {"name": user.username}

        return [u, sess]
    
    return "No user found"

@app.delete("/signout")
def user_signout(session_token:str = Header(), db: Session = Depends(get_db)):
    session = db.query(UserSession).filter(UserSession.session_key == session_token).first()
    if session:
        db.delete(session)
        db.commit()
    return "Signed out"

@app.get("/getAllMovies")
def get_all_movies(db: Session = Depends(get_db)):
    movies = db.query(Movies).all()
    return movies

@app.get("/getMovieByID")
def get_movie_by_id(movie_id:int = Header(), db: Session = Depends(get_db)):
    movie = db.query(Movies).filter(Movies.movie_id == movie_id).first()
    if movie:
        return movie
    return "No movie found"