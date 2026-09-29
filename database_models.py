from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime

Base = declarative_base()


class Driver(Base):
    __tablename__ = 'drivers'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)


class Trip(Base):
    __tablename__ = 'trips'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    trip_type = Column(String)
    start_time = Column(DateTime)
    completion_time = Column(DateTime, nullable=True)
    kilometers = Column(Float, nullable=True)
    earnings = Column(Float, nullable=True)
    completed = Column(Integer, default=0)


class DailyLog(Base):
    __tablename__ = "daily_logs"

    id = Column(Integer, primary_key=True, index=True)
    driver_name = Column(String)
    start_time = Column(DateTime)
    end_time = Column(DateTime, nullable=True)
    fuel_expense = Column(Float, default=0)
    work_hours = Column(Float, default=0)
