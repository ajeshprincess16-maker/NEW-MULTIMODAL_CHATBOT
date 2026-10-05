import React, { useState } from 'react';
import Sidebar from './components/Sidebar';
import ChatArea from './components/ChatArea';
import './App.css';

function App() {
  const [activeMode, setActiveMode] = useState('general');
  const [conversations, setConversations] = useState([]);
  const [activeConversation, setActiveConversation] = useState(null);

  return (
    <div className="app-container">
      <Sidebar 
        conversations={conversations} 
        activeConversation={activeConversation}
        setActiveConversation={setActiveConversation}
      />
      <ChatArea 
        activeMode={activeMode}
        setActiveMode={setActiveMode}
        activeConversation={activeConversation}
      />
    </div>
  );
}

export default App;
