import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './index.css'
import App from './App.tsx'
import Team from './Team.tsx'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <Router>
      <Routes>
        <Route path="/" element = {<App/>} />
        <Route path="/team/:team_name" element = {<Team/>} />
      </Routes>
    </Router>
  </StrictMode>
)
