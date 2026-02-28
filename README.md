# RAG Project with Endee Vector Database

This project implements a Retrieval-Augmented Generation (RAG) system using the Endee vector database and FastAPI.

## Architecture

- **Vector Database**: Endee (running in Docker container)
- **API Framework**: FastAPI
- **Embedding Model**: Sentence Transformers (all-MiniLM-L6-v2)
- **Python Client**: Endee Python SDK

## Setup Instructions

### 1. Start Endee Vector Database

```bash
# From the project root
docker-compose up -d
```

This will start the Endee server on port 8080.

### 2. Set up Python Environment

```bash
cd my-rag-api
pip install -r requirements.txt
```

### 3. Start the API Server

```bash
python run_app.py
```

The API will be available at `http://localhost:8000`

## API Endpoints

### Create Index
```http
POST /create_index
```
Creates a vector index with 384 dimensions (compatible with all-MiniLM-L6-v2).

### Add Document
```http
POST /add_document
```
Adds a document to the vector index.

**Parameters:**
- `text` (string): The document text to add
- `doc_id` (string, optional): Custom document ID

### Search
```http
POST /search
```
Searches for similar documents.

**Body:**
```json
{
  "question": "What is the capital of India?",
  "top_k": 3
}
```

### Health Check
```http
GET /
```
Returns API status.

## Testing

Run the test script to verify the complete RAG pipeline:

```bash
python test_rag.py
```

This will:
1. Create an index
2. Add sample documents about India
3. Perform semantic search queries

## Project Structure

```
rag-project/
├── docker-compose.yml          # Endee container configuration
├── my-rag-api/
│   ├── app.py                 # Main FastAPI application
│   ├── run_app.py            # Server startup script
│   ├── requirements.txt      # Python dependencies
│   ├── test_endee.py         # Endee connection test
│   └── test_rag.py           # Complete RAG pipeline test
├── endee-data/               # Docker volume for vector data
└── README.md                 # This file
```

## How It Works

1. **Document Ingestion**: Text documents are converted to 384-dimensional vectors using Sentence Transformers
2. **Vector Storage**: Vectors are stored in Endee with cosine similarity and float32 precision
3. **Semantic Search**: Queries are converted to vectors and searched against the stored vectors
4. **Results**: Returns the most similar documents with similarity scores

## Configuration

- **Index Name**: `test_index`
- **Embedding Dimension**: 384
- **Similarity Metric**: Cosine
- **Precision**: float32
- **Endee URL**: http://localhost:8080
- **API URL**: http://localhost:8000

## Next Steps

- Add authentication to the API
- Implement document chunking for large texts
- Add metadata filtering
- Create a web interface
- Deploy to production
