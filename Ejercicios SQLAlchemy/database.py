from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


DATEBASE_URL = "sqlite:///escuela.db"
engine = create_engine(DATEBASE_URL, echo=False)

SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass
