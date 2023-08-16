import React, { useState } from 'react';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Typography from '@mui/material/Typography';

const HashtagSearchForm = ({ onSearch }) => {
  const [userName, setUserName] = useState('');
  const [startDate, setStartDate] = useState('2023-07-01');
  const [endDate, setEndDate] = useState('2023-08-01');
  const [atSearch, setAtSearch] = useState('');
  const [hashSearch, setHashSearch] = useState('');

const handleSubmit = (e) => {
    e.preventDefault();
    onSearch({
        userName,
        startDate,
        endDate,
        atSearch: atSearch,
        hashSearch: hashSearch,
    });
};

  const margin = 20
  return (
    <div>
      <Typography variant="h4" style={{marginBottom: margin}}>
        Filtering Facebook Data
      </Typography>
      <form onSubmit={handleSubmit} style={{display: 'flex', flexDirection: 'column'}}>
        <label  style={{marginBottom: margin}}>
          <TextField id="outlined-basic" label="Facebook page" variant="outlined" type="text" value={userName} onChange={(e) => setUserName(e.target.value)} />
        </label>
        <label style={{marginBottom: margin}}>
          Start Date:
          <input type="date" value={startDate} onChange={(e) => setStartDate(e.target.value)} />
        </label>
        <label style={{marginBottom: margin}}>
          End Date:
          <input type="date" value={endDate} onChange={(e) => setEndDate(e.target.value)} />
        </label>
        <label  style={{marginBottom: margin}}>
          <TextField id="outlined-basic" label="@ Search" variant="outlined" input type="text" value={atSearch} onChange={(e) => setAtSearch(e.target.value)} />
        </label>
        <label  style={{marginBottom: margin}}>
          <TextField id="outlined-basic" label="# Search" variant="outlined" type="text" value={hashSearch} onChange={(e) => setHashSearch(e.target.value)} />
        </label>
        <Button variant="contained" type="submit" style={{marginBottom: margin}}>Search</Button>
      </form>
    </div>
  );
};

export default HashtagSearchForm;