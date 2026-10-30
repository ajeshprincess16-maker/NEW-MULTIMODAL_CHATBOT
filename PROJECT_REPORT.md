# Project Report: Multimodal AI Chatbot (MVP)

**Date:** October 30, 2026  
**Repository:** [ajeshprincess16-maker/NEW-MULTIMODAL_CHATBOT](https://github.com/ajeshprincess16-maker/NEW-MULTIMODAL_CHATBOT.git)  
**Branch:** `main`  
**Status:** MVP Initialized & Committed  

---

## 1. Executive Summary

The **Multimodal AI Chatbot** is a beginner-friendly, modular full-stack application designed to demonstrate modern multimodal artificial intelligence capabilities. It brings together interactive conversational AI (text and vision), retrieval-augmented generation (RAG) over user-uploaded documents, web search augmentation, and supportive persona interactions.

The project is intentionally architected to be simple to understand, deploy, and extend, avoiding unnecessary complexity (such as user logins, payment gateways, or enterprise access control) while maintaining production-grade organization standards.

---

## 2. Technology Stack

### Frontend
- **Framework:** React 19 (scaffolded via Vite)
- **Language:** JavaScript (ES6+), HTML5, CSS3
- **Rendering & Markdown:** `react-markdown` for rich AI message responses
- **UI Architecture:** Component-driven structure (`Sidebar`, `ChatArea`, and global layouts) with custom, responsive styling and theme tokens.

### Backend
- **Framework:** FastAPI (Python 3.10+)
- **Server:** Uvicorn ASGI Server
- **Validation & Settings:** Pydantic v2 & `pydantic-settings`
- **AI / LLM Integration:** Hugging Face Inference Client (`huggingface_hub`) integrating `Qwen/Qwen2.5-VL-3B-Instruct`
- **Data & Vector Storage:** PostgreSQL with `pgvector`, managed via SQLAlchemy ORM
- **Utilities:** Python-dotenv, requests, BeautifulSoup4

---

## 3. System Architecture & Directory Structure

```
chatbot.ai/
├── backend/
│   ├── api/                   # API Route endpoints
│   │   ├── chat.py            # Chat and conversation management routes
│   │   ├── documents.py       # Document upload, inspection, and deletion
│   │   ├── health.py          # Service health check endpoint (/api/health)
│   │   └── search.py          # Web search endpoint (/api/search)
│   ├── database/
│   │   └── connection.py      # PostgreSQL / SQLAlchemy engine & session setup
│   ├── models/                # SQLAlchemy database entities
│   │   ├── chat.py            # Conversation and message models
│   │   ├── chunk.py           # Document chunk & vector embedding schemas
│   │   └── document.py        # Document metadata model
│   ├── services/              # Core business and AI logic
│   │   ├── document_service.py# Parsing and chunking logic
│   │   ├── embedding_service.py# Vector embeddings generation
│   │   ├── emotion_service.py # Supportive/emotional conversation tuning
│   │   ├── llm_service.py     # Hugging Face Qwen-VL integration
│   │   ├── rag_service.py     # Vector similarity retrieval
│   │   ├── search_service.py  # Web search querying
│   │   └── vision_service.py  # Image processing helpers
│   ├── config.py              # Environment configuration loader
│   ├── main.py                # FastAPI entrypoint and CORS middleware
│   ├── requirements.txt       # Python package dependencies
│   └── .env.example           # Template for required environment variables
├── frontend/
│   ├── public/                # Static assets
│   ├── src/
│   │   ├── components/        # UI components (Sidebar.jsx, ChatArea.jsx)
│   │   ├── App.jsx            # Main application layout and state
│   │   ├── index.css          # Core design tokens and global styles
│   │   └── main.jsx           # React DOM bootstrap
│   ├── package.json           # Node.js dependencies and scripts
│   └── vite.config.js         # Vite bundler configuration
├── .gitignore                 # Excludes secrets (.env), node_modules, and venv
├── README.md                  # Quickstart documentation
└── PROJECT_REPORT.md          # Comprehensive project report
```

---

## 4. Key Features & Implementation Status

| Feature | Description | Status |
| :--- | :--- | :---: |
| **Interactive Chat** | Real-time AI chat with conversation history and Markdown rendering | ✅ Complete |
| **Multimodal LLM** | Backed by `Qwen/Qwen2.5-VL-3B-Instruct` via Hugging Face Inference API | ✅ Active |
| **Modes Switching** | Support for General, Document, Search, and Supportive modes | ✅ UI & Backend Ready |
| **Document Management & RAG** | Document schemas, chunking definitions, vector tables, and API routes | 🟡 Schema & Endpoints Ready |
| **Web Search** | Search router & service structure configured | 🟡 Service Scaffolded |
| **Security & Git Hygiene** | Sensitive keys (`HF_API_TOKEN`, DB passwords) protected by `.gitignore` | ✅ Configured |

---

## 5. Local Setup & Execution Guide

### Prerequisites
- Node.js (v18+)
- Python (v3.10+)
- PostgreSQL (with `pgvector` extension enabled, optional for pure chat mode)
- A Hugging Face API Token

### 1. Backend Setup
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Set up your environment variables
cp .env.example .env
# Edit .env and supply your HF_API_TOKEN

uvicorn main:app --reload --port 8000
```
*Backend will be available at:* `http://localhost:8000` (Interactive API docs at `http://localhost:8000/docs`)

### 2. Frontend Setup
```bash
cd frontend
npm install
npm run dev
```
*Frontend will be accessible at:* `http://localhost:5173`

---

## 6. Recommendations & Next Steps

1. **Direct Image Upload in UI:** Connect an image upload button to `ChatArea.jsx` so users can send images directly to the Qwen-VL model for visual question answering.
2. **Complete RAG Ingestion Pipeline:** Implement text extraction (PDF/DOCX) in `document_service.py` and store vector embeddings using `pgvector`.
3. **Live Web Search Provider:** Hook `search_service.py` to a real-time provider such as DuckDuckGo or Tavily API to feed fresh web context into chat prompts.
4. **Persistent Chat Sessions:** Link frontend conversation history to the PostgreSQL `/api/conversations` endpoints.
