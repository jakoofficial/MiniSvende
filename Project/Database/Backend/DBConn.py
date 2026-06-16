from sqlalchemy import String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

# Connection
engine = create_engine("mysql+pymysql://root:admin@mysql:3306/minty", echo=True)

class Base(DeclarativeBase):
    pass

# Table
class test(Base):
    __tablename__ = "tester"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Creating the db
Base.metadata.create_all(bind = engine)