from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

url = f"postgresql://postgres:postgres@localhost:5432/postgres"
engine = create_engine(url)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
