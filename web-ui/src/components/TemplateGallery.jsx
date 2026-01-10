import React, { useState } from 'react'
import '../styles/AgentBuilder.css'

const AgentBuilder = () => {
  const [agentConfig, setAgentConfig] = useState({
    name: '',
    description: '',
    instructions: '',
    capabilities: [],
    conversationStarters: [''],
  })

  const capabilities = [
    { id: 'WebSearch', label: 'Web Search', icon: '🔍' },
    { id: 'MicrosoftGraph', label: 'Microsoft Graph', icon: '📊' },
    { id: 'OneDriveAndSharePoint', label: 'OneDrive & SharePoint', icon: '📁' },
    { id: 'GraphConnectors', label: 'Graph Connectors', icon: '🔗' },
  ]

  const toggleCapability = (capId) => {
    setAgentConfig((prev) => ({
      ...prev,
      capabilities: prev.capabilities.includes(capId)
        ? prev.capabilities.filter((c) => c !== capId)
        : [...prev.capabilities, capId],
    }))
  }

  const addConversationStarter = () => {
    setAgentConfig((prev) => ({
      ...prev,
      conversationStarters: [...prev.conversationStarters, ''],
    }))
  }

  const updateConversationStarter = (index, value) => {
    setAgentConfig((prev) => ({
      ...prev,
      conversationStarters: prev.conversationStarters.map((s, i) =>
        i === index ? value : s
      ),
    }))
  }

  const generateAgent = async () => {
    const manifest = {
      $schema: 'https://developer.microsoft.com/json-schemas/copilot/declarative-agent/v1.0/schema.json',
      version: '1.0',
      name: agentConfig.name,
      description: agentConfig.description,
      instructions: agentConfig.instructions,
      capabilities: agentConfig.capabilities.map((cap) => ({ name: cap })),
      conversation_starters: agentConfig.conversationStarters.filter((s) => s.trim()),
    }

    const blob = new Blob([JSON.stringify(manifest, null, 2)], { type: 'application/json' })
    const url = URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = 'declarativeAgent.json'
    a.click()
  }

  return (
    <div className="agent-builder">
      <h2>Declarative Agent Builder</h2>

      <div className="builder-form">
        <div className="form-section">
          <label>Agent Name *</label>
          <input
            type="text"
            maxLength="100"
            placeholder="e.g., Customer Support Agent"
            value={agentConfig.name}
            onChange={(e) => setAgentConfig({ ...agentConfig, name: e.target.value })}
          />
          <span className="char-count">{agentConfig.name.length}/100</span>
        </div>

        <div className="form-section">
          <label>Description *</label>
          <textarea
            maxLength="1000"
            rows="3"
            placeholder="Brief description of what this agent does..."
            value={agentConfig.description}
            onChange={(e) => setAgentConfig({ ...agentConfig, description: e.target.value })}
          />
          <span className="char-count">{agentConfig.description.length}/1000</span>
        </div>

        <div className="form-section">
          <label>Instructions *</label>
          <textarea
            maxLength="8000"
            rows="6"
            placeholder="Detailed instructions for the agent behavior..."
            value={agentConfig.instructions}
            onChange={(e) => setAgentConfig({ ...agentConfig, instructions: e.target.value })}
          />
          <span className="char-count">{agentConfig.instructions.length}/8000</span>
        </div>

        <div className="form-section">
          <label>Capabilities</label>
          <div className="capabilities-grid">
            {capabilities.map((cap) => (
              <button
                key={cap.id}
                className={`capability-btn ${
                  agentConfig.capabilities.includes(cap.id) ? 'active' : ''
                }`}
                onClick={() => toggleCapability(cap.id)}
              >
                <span className="cap-icon">{cap.icon}</span>
                <span>{cap.label}</span>
              </button>
            ))}
          </div>
        </div>

        <div className="form-section">
          <label>Conversation Starters</label>
          {agentConfig.conversationStarters.map((starter, index) => (
            <input
              key={index}
              type="text"
              placeholder={`Starter ${index + 1}`}
              value={starter}
              onChange={(e) => updateConversationStarter(index, e.target.value)}
            />
          ))}
          <button className="add-btn" onClick={addConversationStarter}>
            + Add Conversation Starter
          </button>
        </div>

        <div className="actions">
          <button className="generate-btn" onClick={generateAgent}>
            Generate Agent Manifest
          </button>
          <button
            className="preview-btn"
            onClick={() => alert(JSON.stringify(agentConfig, null, 2))}
          >
            Preview JSON
          </button>
        </div>
      </div>
    </div>
  )
}

export default AgentBuilder
