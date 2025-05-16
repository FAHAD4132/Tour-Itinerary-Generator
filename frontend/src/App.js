import React, { useState } from 'react';
import axios from 'axios';
import ReactMarkdown from 'react-markdown';
import './App.css';

function App() {
  const [url, setUrl] = useState('');
  const [tourData, setTourData] = useState(null);
  const [itinerary, setItinerary] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const fetchTourData = async () => {
    setLoading(true);
    setError('');
    try {
      const response = await axios.post('http://localhost:8000/api/tour', { url });
      setTourData(response.data.data);
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to fetch tour data');
    } finally {
      setLoading(false);
    }
  };

  const generateItinerary = async () => {
    if (!tourData) return;
    setLoading(true);
    setError('');
    try {
      const response = await axios.post('http://localhost:8000/api/generate-itinerary', tourData);
      setItinerary(response.data.itinerary);
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to generate itinerary');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <header className="header">
        <h1>Tour Itinerary Generator</h1>
      </header>
      
      <main className="main-content">
        <div className="input-section">
          <input
            type="text"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            placeholder="Enter tour URL"
          />
          <button onClick={fetchTourData} disabled={loading || !url}>
            {loading ? 'Loading...' : 'Get Tour Data'}
          </button>
        </div>

        {error && <div className="error">{error}</div>}

        {tourData && (
          <div className="tour-data">
            <h2>{tourData.tour_name}</h2>
            <p><strong>Duration:</strong> {tourData.duration}</p>
            <p><strong>Location:</strong> {tourData.location}</p>
            <p><strong>Tour Type:</strong> {tourData.tour_type}</p>
            <p><strong>Trip Category:</strong> {tourData.trip_category}</p>
            <div>
              <strong>Included in the Tour:</strong>
              <ul>
                {tourData.included?.map((item, index) => (
                  <li key={index}>{item}</li>
                ))}
              </ul>
            </div>
            <div>
              <strong>Excluded in the Tour:</strong>
              <ul>
                {tourData.excluded?.map((item, index) => (
                  <li key={index}>{item}</li>
                ))}
              </ul>
            </div>
            <p><strong>Price:</strong> {tourData.price}</p>
            
            <button onClick={generateItinerary} disabled={loading}>
              {loading ? 'Generating...' : 'Generate Itinerary'}
            </button>
          </div>
        )}

        {itinerary && (
          <div className="itinerary">
            <h2>Generated Itinerary</h2>
            <div className="itinerary-content">
              <ReactMarkdown>{itinerary}</ReactMarkdown>
            </div>
          </div>
        )}
      </main>
    </div>
  );
}

export default App;