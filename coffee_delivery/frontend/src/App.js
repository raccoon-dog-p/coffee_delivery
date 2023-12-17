import './App.css';
import NaviBar from './components/NaviBar';
import { BrowserRouter, Route, Switch } from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
    <NaviBar />
    </BrowserRouter>
  );
}

export default App;
