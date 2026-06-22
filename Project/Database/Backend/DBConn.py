from sqlalchemy import Boolean, String, Integer, ForeignKey, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, sessionmaker
import uuid
# Connection
engine = create_engine("mysql+pymysql://root:admin@mysql:3306/minty", echo=True)
# engine = create_engine("mysql+pymysql://root:admin@0.0.0.0:3316/minty", echo=True)

class Base(DeclarativeBase):
    pass

# Table
class test(Base):
    __tablename__ = "tester"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))

class UserSession(Base):
    __tablename__= "user_session"

    session_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    session_key: Mapped[str] = mapped_column(String(32),
                                             default=lambda:str(uuid.uuid4().hex),
                                             unique=True,
                                             index=True
                                             )
    user_id: Mapped[int] = mapped_column(ForeignKey("user_profile.user_id"))
    user: Mapped["UserProfile"] = relationship()

class UserSignin(Base):
    __tablename__= "user_signin"
    
    signin_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    # user_id: Mapped[int] = mapped_column(Integer)
    password: Mapped[str] = mapped_column(String(60))

class UserProfile(Base):
    __tablename__= "user_profile"

    user_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    signin_id: Mapped[int] = mapped_column(ForeignKey("user_signin.signin_id"))
    username: Mapped[str] = mapped_column(String(32))
    signin: Mapped["UserSignin"] = relationship()


class Subscriptions(Base):
    __tablename__= "subscriptions"
    
    sub_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user_profile.user_id"))
    subscription: Mapped[bool] = mapped_column(Boolean, default=False)

class Movies(Base):
    __tablename__= "movies"

    movie_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    movie_title: Mapped[str] = mapped_column(String(100))
    movie_desc: Mapped[str] = mapped_column(String(155))
    movie_link: Mapped[str] = mapped_column(String(250))
    premium: Mapped[bool] = mapped_column(Boolean, default=False)

class Categories(Base):
    __tablename__= "categories"

    category_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    category_title: Mapped[str] = mapped_column(String(50))

class CategoryMovie(Base):
    __tablename__= "category_movie"

    catmov_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.category_id"))
    movie_id: Mapped[int] = mapped_column(ForeignKey("movies.movie_id"))

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Creating the db
Base.metadata.create_all(bind = engine)