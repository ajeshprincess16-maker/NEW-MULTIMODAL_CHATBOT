import React, { useState, useRef, useEffect } from 'react';
import ReactMarkdown from 'react-markdown';
import './ChatArea.css';

function ChatArea({ activeMode, setActiveMode }) {
  const [message, setMessage] = useState('');
  const [messages, setMessages] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSend = async () => {
    if (!message.trim() || isLoading) return;
    
    const userMsg = { role: 'user', content: message };
    // Maintain history except the very new message for the payload
    const currentHistory = messages.map(m => ({ role: m.role, content: m.content }));
    
    setMessages(prev => [...prev, userMsg]);
    setMessage('');
    setIsLoading(true);
    
    try {
        const response = await fetch('http://localhost:8000/api/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ 
                message: userMsg.content, 
                history: currentHistory,
                mode: activeMode 
            })
        });
        const data = await response.json();
        setMessages(prev => [...prev, { role: 'assistant', content: data.response }]);
    } catch (err) {
        setMessages(prev => [...prev, { role: 'assistant', content: '**Error connecting to server.** Please ensure the backend is running and the HF_API_TOKEN is valid.' }]);
    } finally {
        setIsLoading(false);
    }
  };

  const handleClear = () => {
    setMessages([]);
  };

  return (
    <div className="chat-area">
      <div className="mode-selector">
        <select value={activeMode} onChange={(e) => setActiveMode(e.target.value)}>
          <option value="general">General Chat</option>
          <option value="document">Document Chat</option>
          <option value="search">Web Search</option>
          <option value="supportive">Supportive Chat</option>
        </select>
        <button className="clear-btn" onClick={handleClear}>Clear Chat</button>
      </div>
      <div className="messages">
        {messages.map((m, i) => (
          <div key={i} className={`message ${m.role}`}>
            <ReactMarkdown>{m.content}</ReactMarkdown>
          </div>
        ))}
        {isLoading && (
          <div className="message assistant loading">
            <span className="dot"></span><span className="dot"></span><span className="dot"></span>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>
      <div className="input-area">
        <input 
          type="text" 
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Message Multimodal AI..."
          onKeyPress={(e) => e.key === 'Enter' && handleSend()}
          disabled={isLoading}
        />
        <button onClick={handleSend} disabled={isLoading || !message.trim()}>
          {isLoading ? 'Sending...' : 'Send'}
        </button>
      </div>
    </div>
  );
}

export default ChatArea;
