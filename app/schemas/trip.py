from pydantic import BaseModel

class TripCreate(BaseModel):
    destination: str
    start_date: str
    end_date: str

class TripOut(BaseModel):
    id: int
    destination: str
    start_date: str
    end_date: str