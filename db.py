from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

Base = declarative_base()
DB_PATH = "sqlite:///service_platform/neura_platform.db"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String)
    name = Column(String)
    password = Column(String)  # Store hashed passwords!
    role = Column(String, default="operator")

class WorkflowHistory(Base):
    __tablename__ = "workflow_history"
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    user = Column(String)
    workflow = Column(Text)
    result = Column(Text)

engine = create_engine(DB_PATH, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
def init_db():
    Base.metadata.create_all(engine)
