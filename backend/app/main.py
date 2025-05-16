from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .scraper import scrape_tour_data
from .itinerary import generate_itinerary

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TourRequest(BaseModel):
    url: str

@app.post("/api/tour")
async def get_tour_data(request: TourRequest):
    try:
        tour_data = scrape_tour_data(request.url)
        return {"success": True, "data": tour_data}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/generate-itinerary")
async def generate_tour_itinerary(tour_data: dict):
    try:
        itinerary = generate_itinerary(tour_data)
        return {"success": True, "itinerary": itinerary}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy"}