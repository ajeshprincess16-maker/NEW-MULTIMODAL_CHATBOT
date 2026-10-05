# Multimodal AI Chatbot

A beginner-friendly Multimodal AI Chatbot built using React, FastAPI, Python and PostgreSQL.

## Features
- AI Chat (Text & Image)
- RAG-Based Document Q&A
- Document Management
- Web Search integration
- Supportive emotional chat mode

## Tech Stack
- Frontend: React (Vite), HTML/CSS
- Backend: FastAPI, Python, PostgreSQL, pgvector

## Setup Instructions

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
# Copy .env.example to .env and fill in your keys
cp .env.example .env
uvicorn main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```
