import React, { useCallback, useState } from 'react'
import ReactFlow, {
  addEdge,
  MiniMap,
  Controls,
  Background,
  useNodesState,
  useEdgesState,
} from 'react-flow-renderer'
import '../styles/WorkflowDesigner.css'

const initialNodes = [
  {
    id: '1',
    type: 'input',
    data: { label: 'Start: User Query' },
    position: { x: 250, y: 0 },
  },
]

const initialEdges = []

const nodeTypes = [
  { type: 'trigger', label: 'Trigger', icon: '▶' },
  { type: 'action', label: 'Action', icon: '⚡' },
  { type: 'condition', label: 'Condition', icon: '◇' },
  { type: 'api', label: 'API Call', icon: '🔌' },
  { type: 'graph', label: 'Graph Query', icon: '📊' },
  { type: 'response', label: 'Response', icon: '💬' },
]

const WorkflowDesigner = () => {
  const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes)
  const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges)
  const [selectedNodeType, setSelectedNodeType] = useState('action')

  const onConnect = useCallback(
    (params) => setEdges((eds) => addEdge(params, eds)),
    [setEdges]
  )

  const addNode = () => {
    const newNode = {
      id: `${nodes.length + 1}`,
      type: selectedNodeType === 'condition' ? 'default' : 'default',
      data: { 
        label: `${selectedNodeType.charAt(0).toUpperCase() + selectedNodeType.slice(1)} Node ${nodes.length + 1}`,
      },
      position: {
        x: Math.random() * 400 + 100,
        y: Math.random() * 400 + 100,
      },
    }
    setNodes((nds) => nds.concat(newNode))
  }

  const exportWorkflow = () => {
    const workflow = {
      nodes: nodes,
      edges: edges,
      metadata: {
        name: 'Agent Workflow',
        version: '1.0',
        created: new Date().toISOString(),
      },
    }
    const blob = new Blob([JSON.stringify(workflow, null, 2)], { type: 'application/json' })
    const url = URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = 'workflow.json'
    a.click()
  }

  return (
    <div className="workflow-designer">
      <div className="toolbar">
        <h2>Visual Workflow Designer</h2>
        <div className="node-palette">
          <h3>Add Nodes:</h3>
          <div className="node-buttons">
            {nodeTypes.map((node) => (
              <button
                key={node.type}
                className={`node-btn ${selectedNodeType === node.type ? 'active' : ''}`}
                onClick={() => setSelectedNodeType(node.type)}
              >
                <span className="node-icon">{node.icon}</span>
                {node.label}
              </button>
            ))}
          </div>
          <button className="add-node-btn" onClick={addNode}>
            + Add {selectedNodeType} Node
          </button>
        </div>
        <div className="actions">
          <button onClick={exportWorkflow}>Export Workflow</button>
          <button onClick={() => { setNodes(initialNodes); setEdges(initialEdges); }}>
            Clear Canvas
          </button>
        </div>
      </div>

      <div className="canvas">
        <ReactFlow
          nodes={nodes}
          edges={edges}
          onNodesChange={onNodesChange}
          onEdgesChange={onEdgesChange}
          onConnect={onConnect}
          fitView
        >
          <Background />
          <Controls />
          <MiniMap />
        </ReactFlow>
      </div>

      <div className="properties-panel">
        <h3>Node Properties</h3>
        <p>Select a node to edit its properties</p>
        <div className="property-form">
          <label>Name:</label>
          <input type="text" placeholder="Node name" />
          <label>Description:</label>
          <textarea placeholder="Node description" rows="3" />
          <label>Action Type:</label>
          <select>
            <option>Send Message</option>
            <option>Query Graph API</option>
            <option>Call Custom API</option>
            <option>Check Condition</option>
          </select>
        </div>
      </div>
    </div>
  )
}

export default WorkflowDesigner
