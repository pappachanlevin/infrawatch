import os
from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float, DateTime
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = (
    f"postgresql://{os.environ['POSTGRES_USER']}"
    f":{os.environ['POSTGRES_PASSWORD']}"
    f"@{os.environ['POSTGRES_HOST']}"
    f":{os.environ['POSTGRES_PORT']}"
    f"/{os.environ['POSTGRES_DB']}"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

class PingResult(Base):
    __tablename__ = "ping_results"
    id          = Column(Integer, primary_key=True)
    url         = Column(String, nullable=False)
    is_up       = Column(Boolean, nullable=False)
    status_code = Column(Integer)
    response_ms = Column(Float)
    checked_at  = Column(DateTime, default=datetime.utcnow)

def init_db():
    Base.metadata.create_all(bind=engine)