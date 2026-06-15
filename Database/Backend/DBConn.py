from sqlalchemy import String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


engine = create_engine("sqlite:///./data.db", echo=True)

class Base(DeclarativeBase):
    pass

class test(Base):
    __tablename__ = "tester"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))


Base.metadata.create_all(bind = engine)