import React, { useState } from 'react';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Typography from '@mui/material/Typography';
import CircularProgress from '@mui/material/CircularProgress';

const SearchForm = ({ onSearch, loading }) => {
  const [query, setQuery] = useState('');
  const [startDate, setStartDate] = useState('2023-07-01');

  const handleSubmit = (e) => {
    e.preventDefault();
    onSearch({ query, startDate });
  };

  const margin = 20
  return (
    <div>
      <Typography variant="h4" style={{marginBottom: margin}}>
        Scraping Facebook Data
      </Typography>
      <form onSubmit={handleSubmit} style={{display: 'flex', flexDirection: 'column'}}>
        
        <TextField id="outlined-basic" label="Facebook page" variant="outlined"
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          style={{marginBottom: margin}}
        />
        <label style={{marginBottom: margin}}>
          Start Date:
          <input
            type="date"
            value={startDate}
            onChange={(e) => setStartDate(e.target.value)}
          />
        </label>
        <Button variant="contained" type="submit" style={{marginBottom: margin}}>
          {loading ? <CircularProgress style={{color: "white"}} />: "Search"}
        </Button>
      </form>
    </div>
  );
};

export default SearchForm;