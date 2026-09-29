from pydantic import BaseModel


class Driver(BaseModel):
    name: str


class Trip(BaseModel):
    trip_title: str
    trip_type: str


class Complete(BaseModel):
    kilometers: float
    earnings: float


class End(BaseModel):
    fuel_expense: float
