import React from 'react'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import ShortenerForm from './components/ShortenerForm'
import './index.css'

function App() {
  return (
    <BrowserRouter>
      <div className="container">
        <Routes>
          <Route path="/" element={<ShortenerForm />} />
        </Routes>
      </div>
    </BrowserRouter>
  )
}

export default App
