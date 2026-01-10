import React, { useState, useEffect } from 'react'
import '../styles/TemplateGallery.css'

const TemplateGallery = () => {
  const [templates, setTemplates] = useState([])
  const [filter, setFilter] = useState('all')
  const [searchTerm, setSearchTerm] = useState('')

  useEffect(() => {
    // In production, this would fetch from the marketplace API
    fetchTemplates()
  }, [])

  const fetchTemplates = async () => {
    // Mock data - in production would call: GET /api/marketplace/templates
    const mockTemplates = [
      {
        id: 1,
        name: 'Customer Support Agent',
        category: 'Support',
        description: 'Automated customer support with ticket management',
        author: 'Microsoft',
        downloads: 1523,
        rating: 4.8,
        featured: true,
      },
      {
        id: 2,
        name: 'Sales Assistant',
        category: 'Sales',
        description: 'Lead qualification and CRM integration',
        author: 'Community',
        downloads: 892,
        rating: 4.5,
        featured: true,
      },
      {
        id: 3,
        name: 'HR Onboarding Bot',
        category: 'HR',
        description: 'Streamlined employee onboarding process',
        author: 'Microsoft',
        downloads: 654,
        rating: 4.7,
        featured: false,
      },
      {
        id: 4,
        name: 'Data Analytics Agent',
        category: 'Analytics',
        description: 'Query and visualize business data',
        author: 'Community',
        downloads: 423,
        rating: 4.3,
        featured: false,
      },
      {
        id: 5,
        name: 'Meeting Insights Bot',
        category: 'Productivity',
        description: 'Extract action items and summaries from meetings',
        author: 'Microsoft',
        downloads: 1203,
        rating: 4.9,
        featured: true,
      },
    ]
    setTemplates(mockTemplates)
  }

  const filteredTemplates = templates.filter((t) => {
    const matchesFilter = filter === 'all' || t.category === filter
    const matchesSearch = t.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
      t.description.toLowerCase().includes(searchTerm.toLowerCase())
    return matchesFilter && matchesSearch
  })

  const importTemplate = async (templateId) => {
    // In production: POST /api/marketplace/import/{templateId}
    alert(`Importing template ${templateId}... This would download and set up the agent locally.`)
  }

  return (
    <div className="template-gallery">
      <div className="gallery-header">
        <h2>Community Templates Marketplace</h2>
        <div className="search-bar">
          <input
            type="text"
            placeholder="Search templates..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
          />
        </div>
      </div>

      <div className="filters">
        <button
          className={filter === 'all' ? 'active' : ''}
          onClick={() => setFilter('all')}
        >
          All
        </button>
        <button
          className={filter === 'Support' ? 'active' : ''}
          onClick={() => setFilter('Support')}
        >
          Support
        </button>
        <button
          className={filter === 'Sales' ? 'active' : ''}
          onClick={() => setFilter('Sales')}
        >
          Sales
        </button>
        <button
          className={filter === 'HR' ? 'active' : ''}
          onClick={() => setFilter('HR')}
        >
          HR
        </button>
        <button
          className={filter === 'Analytics' ? 'active' : ''}
          onClick={() => setFilter('Analytics')}
        >
          Analytics
        </button>
        <button
          className={filter === 'Productivity' ? 'active' : ''}
          onClick={() => setFilter('Productivity')}
        >
          Productivity
        </button>
      </div>

      <div className="templates-grid">
        {filteredTemplates.map((template) => (
          <div key={template.id} className={`template-card ${template.featured ? 'featured' : ''}`}>
            {template.featured && <span className="badge">Featured</span>}
            <h3>{template.name}</h3>
            <p className="category">{template.category}</p>
            <p className="description">{template.description}</p>
            <div className="meta">
              <span>By {template.author}</span>
              <span>⭐ {template.rating}</span>
              <span>⬇ {template.downloads}</span>
            </div>
            <button
              className="import-btn"
              onClick={() => importTemplate(template.id)}
            >
              Import Template
            </button>
          </div>
        ))}
      </div>
    </div>
  )
}

export default TemplateGallery
