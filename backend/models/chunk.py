from sqlalchemy import Column, Integer, Text, ForeignKey
# If using pgvector, we would import Vector type
# from pgvector.sqlalchemy import Vector
from .chat import Base
from datetime import datetime
from sqlalchemy import DateTime

class DocumentChunk(Base):
    __tablename__ = 'document_chunks'
    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(Integer, ForeignKey('documents.id'))
    content = Column(Text)
    chunk_index = Column(Integer)
    # embedding = Column(Vector(1536)) # Uncomment when pgvector is active
    created_at = Column(DateTime, default=datetime.utcnow)
