import logo from './logo.svg';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import React from 'react';
import Dashboard from './Dashboard/Dashboard';
import './App.css';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/dashboard" element={<Dashboard />}></Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;