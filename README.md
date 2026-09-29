# 🚗 Trip Logging System

A REST API built with **FastAPI, SQLAlchemy, and PostgreSQL** for managing driver working days and trips.

## 📌 Features

* Start a driver's working day
* Record driver name and start time
* Create new trips
* Track trip type and title
* Complete trips with:

  * Kilometers covered
  * Trip earnings
  * Completion time
* End the driver's working day
* Record fuel expense
* Calculate total working hours
* Store data in PostgreSQL

## 🛠️ Technologies

* Python
* FastAPI
* SQLAlchemy
* PostgreSQL
* Pydantic
* Uvicorn

## 📂 Project Structure

```text
trip-logging-system/
│
├── assignment.py
├── model.py
├── database_models.py
├── database1.py
└── README.md
```

## 🔗 API Endpoints

### Start Day

```http
POST /startday
```

Starts a driver's working day and records the current time.

### Create Trip

```http
POST /createtrip
```

Creates a new trip with its title, type, and start time.

### Complete Trip

```http
PUT /trips/{trip_id}/complete
```

Completes a trip and records kilometers, earnings, and completion time.

### End Day

```http
POST /end-day
```

Ends the active working day, records fuel expense, and calculates working hours.

## 🗄️ Database

The application uses PostgreSQL with SQLAlchemy. The database contains models for:

* `Driver`
* `Trip`
* `DailyLog`

The `Trip` model stores trip information including start time, completion time, kilometers, earnings, and completion status.

The `DailyLog` model stores driver name, start/end time, fuel expense, and work hours.

## ⚙️ Database Configuration

Update the PostgreSQL connection string in `database1.py`:

```python
db_url = "postgresql://postgres:root@localhost:5432/main"
```

The project uses SQLAlchemy's `create_engine()` and `sessionmaker()` to connect to PostgreSQL.

## ▶️ Run the Project

Install dependencies:

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic
```

Start the FastAPI server:

```bash
uvicorn assignment:app --reload
```

Open the API documentation:

```text
http://127.0.0.1:8000/docs
```

## 📊 Working Hours

Working hours are calculated when the driver ends the day:

```python
duration = daily_log.end_time - daily_log.start_time
daily_log.work_hours = duration.total_seconds() / 3600
```

This calculates the difference between the recorded start and end times in hours.

## 👨‍💻 Project

A backend REST API project demonstrating **FastAPI + SQLAlchemy + PostgreSQL** integration for a driver trip and daily activity logging system.
