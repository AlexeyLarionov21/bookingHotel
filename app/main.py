from fastapi import FastAPI, Query, Depends
from datetime import date
from pydantic import BaseModel
from app.bookings.router import router as router_bookings
from app.users.router import router as router_users

app = FastAPI()
app.include_router(router_users)
app.include_router(router_bookings)

class GETHotelsSearchArgs:
    def __init__(
            self,
            location: str,
            date_from: date, 
            date_to: date,
            has_spa: bool = None,    
            stars: int = Query(None, ge=1.0, le=5.0, description="rate of hotels")
    ):    
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.has_spa = has_spa
        self.stars = stars

class SHotel(BaseModel):
    address: str
    name: str
    stars: int

@app.get("/hotels")
def get_hotels(search_args: GETHotelsSearchArgs = Depends()):
    return search_args

class SBooking(BaseModel):
    room_id: int
    date_from: date 
    date_to: date
    

@app.post("/bookings")
def add_booking(booking: SBooking):
    pass