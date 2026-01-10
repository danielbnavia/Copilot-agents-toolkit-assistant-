import React, { useState } from 'react'
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom'
import WorkflowDesigner from './components/WorkflowDesigner'
import AgentBuilder from './components/AgentBuilder'
import TemplateGallery from './components/TemplateGallery'
import './App.css'

function App() {
  const [activeTab, setActiveTab] = useState('designer')

  return (
    <Router>
      <div className="app">
        <header className="app-header">
          <h1>Microsoft 365 Agent Toolkit</h1>
          <nav>
            <Link to="/" className={activeTab === 'designer' ? 'active' : ''} onClick={() => setActiveTab('designer')}>
              Workflow Designer
            </Link>
            <Link to="/builder" className={activeTab === 'builder' ? 'active' : ''} onClick={() => setActiveTab('builder')}>
              Agent Builder
            </Link>
            <Link to="/templates" className={activeTab === 'templates' ? 'active' : ''} onClick={() => setActiveTab('templates')}>
              Template Gallery
            </Link>
          </nav>
        </header>

        <main className="app-main">
          <Routes>
            <Route path="/" element={<WorkflowDesigner />} />
            <Route path="/builder" element={<AgentBuilder />} />
            <Route path="/templates" element={<TemplateGallery />} />
          </Routes>
        </main>
      </div>
    </Router>
  )
}

export default App
