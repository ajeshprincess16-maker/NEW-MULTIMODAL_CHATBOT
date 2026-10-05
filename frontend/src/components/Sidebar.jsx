import React from 'react';
import './Sidebar.css';

function Sidebar({ conversations, activeConversation, setActiveConversation }) {
  return (
    <div className="sidebar">
      <button className="new-chat-btn">
        + New Chat
      </button>
      <div className="documents-section">
        <h3>Documents</h3>
        <button className="attach-btn">📎 Upload Document</button>
      </div>
    </div>
  );
}

export default Sidebar;
