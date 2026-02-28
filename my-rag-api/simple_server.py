from fastapi import FastAPI
from pydantic import BaseModel
from endee import Endee
from sentence_transformers import SentenceTransformer

app = FastAPI(title="RAG API with Endee")

# Load embedding model
print("Loading embedding model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

# Initialize Endee client
print("Connecting to Endee...")
client = Endee()
INDEX_NAME = "test_index"

class Query(BaseModel):
    question: str
    top_k: int = 3

@app.get("/")
def root():
    return {"message": "RAG API is running", "status": "ok"}

@app.post("/search")
def search(query: Query):
    print(f"Searching for: {query.question}")
    try:
        # Convert question to embedding
        vector = model.encode(query.question).tolist()
        
        # Get index and search in Endee
        index = client.get_index(name=INDEX_NAME)
        results = index.query(vector=vector, top_k=query.top_k)
        
        return {
            "question": query.question,
            "results": results
        }
    except Exception as e:
        print(f"Search error: {e}")
        return {"error": "Search failed", "details": str(e)}

@app.post("/add_document")
def add_document(text: str, doc_id: str = None):
    print(f"Adding document: {text[:50]}...")
    try:
        # Generate embedding
        vector = model.encode(text).tolist()
        
        # Get index
        index = client.get_index(name=INDEX_NAME)
        
        # Add vector using upsert
        index.upsert([{
            "id": doc_id or text[:20],
            "vector": vector,
            "meta": {"text": text}
        }])
        
        return {
            "status": "added",
            "doc_id": doc_id or text[:20],
            "message": "Document added successfully"
        }
    except Exception as e:
        print(f"Add error: {e}")
        return {
            "status": "failed",
            "error": str(e)
        }

@app.post("/create_index")
def create_index():
    print("Creating index...")
    try:
        # Create index
        client.create_index(
            name=INDEX_NAME,
            dimension=384,
            space_type="cosine",
            precision="float32"
        )
        
        return {
            "status": "created",
            "index_name": INDEX_NAME,
            "message": "Index created successfully"
        }
    except Exception as e:
        print(f"Create error: {e}")
        return {
            "status": "failed",
            "error": str(e)
        }

if __name__ == "__main__":
    import uvicorn
    print("Starting server on http://0.0.0.0:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)
