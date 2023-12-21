import './App.css';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import NaviBar from './components/NaviBar';
import SignUp from './pages/SignUp';
import Home from './pages/Main';
import React from 'react';

function App() {
  return (
    <BrowserRouter>
    <NaviBar />
    <Routes>
      <Route exact path='/' element={<Home />}></Route>
      <Route exact path='/signin' element={<SignUp />}></Route>
    </Routes>
    </BrowserRouter>
  );
}

export default App;
