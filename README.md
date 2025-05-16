# Tour Itinerary Generator 🌍✈️

A web application that scrapes tour information from Mezwalah websites and generates detailed day-by-day itineraries using LLM.

![image](https://github.com/user-attachments/assets/70d16ce7-4c3a-4141-969b-95b0343149b4)

## Features

- **Tour Data Scraping**: Extracts key information from tour URLs including:
  - Tour name, duration, and location
  - Included/excluded items
  - Pricing information
- **LLM-Powered Itinerary Generation**: Creates detailed day-by-day itineraries with:
  - Morning/afternoon/evening activities
  - Meal plans
  - Accommodation details
- **User-Friendly Interface**: Simple React frontend to submit URLs and view results
- **Markdown Support**: Beautifully formatted itinerary output

## Tech Stack

**Backend**:
- Python 3.x
- FastAPI (REST API framework)
- BeautifulSoup (web scraping)
- LangChain + Ollama (LLM itinerary generation)
- Pydantic (data validation)

**Frontend**:
- React.js
- Axios (API calls)
- ReactMarkdown (itinerary rendering)

## Prerequisites

Before running the project, ensure you have:

- Python 3.8+ installed
- Node.js (for frontend)
- Ollama installed and running with the `llama3.2` model:
  ```bash
  ollama pull llama3.2

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/FAHAD4132/TourIitinerary-Generator.git
   cd tour-itinerary-generator
   ```

2. **Backend Setup**:
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Frontend Setup**:
   ```bash
   cd ../frontend
   npm install
   ```

## Running the Application

1. **Start the backend server** (from backend directory):
   ```bash
   uvicorn app.main:app --reload
   ```
   The API will run on `http://localhost:8000`

2. **Start the frontend** (from frontend directory):
   ```bash
   npm start
   ```
   The React app will open in your browser at `http://localhost:3000`

## Usage

1. Enter a valid tour URL from Mezwalah websites in the input field
2. Click "Get Tour Data" to scrape the tour information
3. Review the extracted tour data
4. Click "Generate Itinerary" to create a detailed day-by-day plan
5. View the beautifully formatted itinerary

## API Endpoints

- `POST /api/tour`: Submit a tour URL to scrape data
  ```json
  {
    "url": "https://www.mezwalah.com/trips/discovering-riyadh"
  }
  ```
  
- `POST /api/generate-itinerary`: Generate itinerary from tour data
  ```json
  {
    "tour_name": "Riyadh Trip | The World Gate V2",
    "duration": "3 Days",
    "tour_type": "City Tours",
    "trip_category": "private",
    "location": "Riyadh",
    "included": ["Transportation", "Tour Guide", "Activites mentioned in the itinerary"],
    "excluded": ["Flight Tickets (International/Domestic)", "Meals", "Accommodation", "Activites not mentioned in the itinerary"],
    "price": "2,793 SAR"
  }
  ```

- `GET /health`: Health check endpoint

## Acknowledgments

- BeautifulSoup for web scraping capabilities
- Ollama for providing the LLM infrastructure
- FastAPI for the efficient backend framework
