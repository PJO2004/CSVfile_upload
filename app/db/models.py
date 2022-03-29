from .database import Base
from sqlalchemy import Column, Integer, String, Numeric


class test(Base):
	__tablename__ = "test"

	Index = Column(Integer, primary_key=True, index=True)
	date = Column(String(15), unique=False)
	Point = Column(Integer, unique=False)
	average_temperature_ = Column(Numeric, unique=False)
	minimum_temperature_ = Column(Numeric, unique=False)
	maximum_temperature_ = Column(Numeric, unique=False)
