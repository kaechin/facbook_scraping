import React, { useState } from 'react';
import './App.css';
import SearchForm from './SearchForm';
import HashtagSearchForm from './HashtagSearchForm';
import Button from '@mui/material/Button';
import Paper from '@mui/material/Paper';
import Typography from '@mui/material/Typography';

function App() {
  const [result, setResult] = useState('');
  const [currentQuery, setCurrentQuery] = useState('');
  const [loading, setLoading] = useState(false)

  const displayTemporaryMessage = (message, duration = 30000) => {
    setResult(message);
    setTimeout(() => {
      setResult('');  // clear the message after the given duration
    }, duration);
  };

  const handleSearch = async ({ query, startDate }) => {
    try {
      setLoading(true)
      const response = await fetch(`http://localhost:5000/api/search?q=${query}&start_date=${startDate}`);
      const data = await response.json();
      if (data.status === "success") {
        displayTemporaryMessage(data.message.message || data.message);
        // Store the query in the state to be used later for downloading CSV
        setCurrentQuery(query);
      } else {
        displayTemporaryMessage(data.message || "Error fetching data.");
      }
      setLoading(false)

    } catch (error) {
      console.error("Error fetching data:", error);
      displayTemporaryMessage("Error fetching data.");
      setLoading(false)

    }
  };


const handleHashtagSearch = async ({ userName, startDate, endDate, atSearch, hashSearch }) => {
  if (!userName || !startDate || !endDate) {
    displayTemporaryMessage("Please fill in all the fields.");
    return;
  }
  try {
    const response = await fetch(`http://localhost:5000/api/hashtags?username=${userName}&start_date=${startDate}&end_date=${endDate}&at_hashtags=${atSearch}&hash_hashtags=${hashSearch}`);
    const data = await response.json();
    if (data.status === "success") {
      displayTemporaryMessage(data.message.message || data.message);
      // Store the username in the state to be used later for downloading CSV
      setCurrentQuery(userName);
    } else {
      displayTemporaryMessage(data.message || "Error fetching hashtag data.");
    }
  } catch (error) {
    console.error("Error fetching hashtag data:", error);
    displayTemporaryMessage("Error fetching hashtag data.");
  }
};


  const handlePageDownload = async () => {
    try {
      const response = await fetch(`http://localhost:5000/api/download/${currentQuery}.csv`);
      const blob = await response.blob();
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `${currentQuery}.csv`;
      a.click();
      displayTemporaryMessage("CSV Downloaded Successfully!");
    } catch (error) {
      displayTemporaryMessage("Error downloading CSV.");
    }
  };

  const handleHashtagDownload = async () => {
    console.log(`currentQuery value: ${currentQuery}`);

    if(!currentQuery || currentQuery === "undefined") {
        displayTemporaryMessage("Invalid username or query. Please try again.");
        return;
    }

    try {
        const response = await fetch(`http://localhost:5000/api/download/${currentQuery}_hashtag.csv`);

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const text = await response.text();

        const blob = new Blob([text], { type: 'text/csv' });
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `${currentQuery}_hashtag.csv`;
        a.click();
        displayTemporaryMessage("CSV Downloaded Successfully!");

    } catch (error) {
        displayTemporaryMessage(`Error downloading CSV: ${error.message}`);
    }
};

  const margin = 30
  return (
    <div className="App">
        <header className="App-header">
        <Typography variant="h2" style={{marginBottom: margin, marginTop: margin}}>
        Facebook Page Scraper
        </Typography>
        </header>
        <div style={{display: 'flex', margin: "auto", width: 750}}>
          <Paper style={{padding: 30, margin: margin, width: 250}}>
            <SearchForm onSearch={handleSearch} loading={loading} />
            {!currentQuery ? null :
              <Button variant="contained" onClick={handlePageDownload} disabled={!currentQuery}>Download Page CSV</Button>
            }
            </Paper>
          <Paper style={{padding: 30, margin: margin, width: 250}}>
            <HashtagSearchForm onSearch={handleHashtagSearch} />
            <Button variant="contained" onClick={handleHashtagDownload} disabled={!currentQuery}>Download Hashtag CSV</Button>
          </Paper>
        </div>
        <div>
            <pre>{result}</pre>
        </div>
    </div>
);

}

export default App;




