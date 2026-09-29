from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from model import Driver, Trip, Complete, End
from datetime import datetime
from database1 import engine, session
import database_models

app = FastAPI()
database_models.Base.metadata.create_all(bind=engine)

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


@app.get('/into')
def intro():
    print('TRIP LOGGING APPLICATION')


@app.post('/startday')
def start_Day(driver: Driver, db: Session = Depends(get_db)):
    daily_log = database_models.DailyLog(
        driver_name=driver.name,
        start_time=datetime.now()
    )
    db.add(daily_log)
    db.commit()
    db.refresh(daily_log)

    return {
        "message": 'Driver started successfully',
        'Driver name': daily_log.driver_name,
        'Start Time': daily_log.start_time
    }


@app.post('/createtrip')
def create_trip(trip: Trip, db: Session = Depends(get_db)):
    new_trip = database_models.Trip(
        title=trip.trip_title,
        trip_type=trip.trip_type,
        start_time=datetime.now(),
        completed=0
    )
    db.add(new_trip)
    db.commit()
    db.refresh(new_trip)

    return {
        "message": "Trip created successfully",
        "trip_id": new_trip.id,
        "title": new_trip.title,
        "trip_type": new_trip.trip_type,
        "start_time": new_trip.start_time
    }


@app.put("/trips/{trip_id}/complete")
def complete_trip(
    trip_id: int,
    trip: Complete,
    db: Session = Depends(get_db)
):
    db_trip = (
        db.query(database_models.Trip)
        .filter(database_models.Trip.id == trip_id)
        .first()
    )

    if db_trip is None:
        return {
            "message": "Trip not found"
        }

    db_trip.kilometers = trip.kilometers
    db_trip.earnings = trip.earnings
    db_trip.completion_time = datetime.now()
    db_trip.completed = 1

    db.commit()
    db.refresh(db_trip)

    return {
        "message": "Trip completed successfully",
        "trip_id": db_trip.id,
        "title": db_trip.title,
        "trip_type": db_trip.trip_type,
        "kilometers": db_trip.kilometers,
        "earnings": db_trip.earnings,
        "completion_time": db_trip.completion_time
    }


@app.post("/end-day")
def end_day(
    data: End,
    db: Session = Depends(get_db)
):
    daily_log = (
        db.query(database_models.DailyLog)
        .filter(
            database_models.DailyLog.end_time == None
        )
        .order_by(
            database_models.DailyLog.id.desc()
        )
        .first()
    )

    if daily_log is None:
        return {
            "message": "No active day found"
        }

    daily_log.end_time = datetime.now()
    daily_log.fuel_expense = data.fuel_expense

    duration = daily_log.end_time - daily_log.start_time
    daily_log.work_hours = duration.total_seconds() / 3600

    db.commit()
    db.refresh(daily_log)

    return {
        "message": "Day ended successfully",
        "fuel_expense": daily_log.fuel_expense,
        "end_time": daily_log.end_time,
        "work_hours": daily_log.work_hours
    }
