# RAG Application with Endee Vector Database

A complete Retrieval-Augmented Generation (RAG) system built with FastAPI and Endee vector database.

## Features

- **Vector Database**: Endee (high-performance vector storage)
- **API Framework**: FastAPI with automatic Swagger documentation
- **Embeddings**: Sentence Transformers (all-MiniLM-L6-v2)
- **Semantic Search**: Cosine similarity with 384-dimensional vectors

## Prerequisites

- Docker Desktop (for Endee container)
- Python 3.8+
- Git

## Quick Start

### 1. Clone & Setup
```bash
git clone https://github.com/AnjeshDash/Rag-application.git
cd Rag-application
```

### 2. Start Vector Database
```bash
docker-compose up -d
```
This starts Endee on port 8080.

### 3. Install Dependencies
```bash
cd my-rag-api
pip install -r requirements.txt
```

### 4. Start API Server
```bash
python simple_server.py
```
API runs on http://localhost:8000

## API Documentation

Visit http://localhost:8000/docs for interactive Swagger UI.

### Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| POST | `/create_index` | Create vector index |
| POST | `/add_document` | Add document to index |
| POST | `/search` | Semantic search |

### Usage Examples

#### Add Document
```bash
curl -X POST "http://localhost:8000/add_document?text=Your document here&doc_id=unique_id"
```

#### Search
```bash
curl -X POST -H "Content-Type: application/json" \
     -d '{"question":"What is India?","top_k":3}' \
     http://localhost:8000/search
```

## Testing

Run the test script:
```bash
python test_api.py
```

This will:
- Create index (if needed)
- Add sample documents
- Test semantic search queries

## Project Structure

```
rag-application/
├── docker-compose.yml      # Endee container setup
├── my-rag-api/
│   ├── app.py           # Main FastAPI application
│   ├── simple_server.py  # Standalone server with logging
│   ├── test_api.py      # Complete API test suite
│   └── requirements.txt # Python dependencies
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## Configuration

- **Index Name**: `test_index`
- **Vector Dimension**: 384 (all-MiniLM-L6-v2)
- **Similarity**: Cosine
- **Precision**: float32
- **Endee URL**: http://localhost:8080
- **API URL**: http://localhost:8000

## Development

### Adding New Endpoints
1. Edit `app.py` or `simple_server.py`
2. Add your FastAPI route
3. Restart server

### Custom Embeddings
Change the model in `simple_server.py`:
```python
model = SentenceTransformer("your-model-name")
```

## Troubleshooting

### Port Already in Use
```bash
# Kill processes on ports 8000 or 8080
netstat -ano | findstr :8000
netstat -ano | findstr :8080
```

### Docker Issues
```bash
# Reset Docker containers
docker-compose down
docker system prune -f
docker-compose up -d
```

### Python Dependencies
```bash
# Fresh install
pip install -r requirements.txt --force-reinstall
```

## Contributing

1. Fork the repository
2. Create feature branch
3. Make changes
4. Test thoroughly
5. Submit pull request

## License

This project is open source and available under the MIT License.

## Acknowledgments

- [Endee](https://endee.io) - High-performance vector database
- [Sentence Transformers](https://sbert.net/) - Text embeddings
- [FastAPI](https://fastapi.tiangolo.com/) - Modern web framework
