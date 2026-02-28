import requests

# Test API endpoints
base_url = "http://localhost:8000"

print("Testing RAG API...")
print("=" * 50)

# 1. Health check
print("\n1. Health Check:")
response = requests.get(f"{base_url}/")
print(f"Status: {response.status_code}")
print(f"Response: {response.json()}")

# 2. Create index (might fail if already exists)
print("\n2. Create Index:")
response = requests.post(f"{base_url}/create_index")
print(f"Status: {response.status_code}")
print(f"Response: {response.json()}")

# 3. Add documents
print("\n3. Adding Documents:")
documents = [
    ("The capital of India is New Delhi.", "doc1"),
    ("Mumbai is the financial capital of India.", "doc2"),
    ("The Taj Mahal is located in Agra.", "doc3"),
    ("Bengaluru is known as the Silicon Valley of India.", "doc4")
]

for text, doc_id in documents:
    response = requests.post(f"{base_url}/add_document", params={"text": text, "doc_id": doc_id})
    print(f"Added {doc_id}: {response.status_code} - {response.json()}")

# 4. Search
print("\n4. Testing Search:")
queries = [
    "What is the capital of India?",
    "Where is the Taj Mahal located?",
    "Which city is called Silicon Valley of India?"
]

for query in queries:
    payload = {"question": query, "top_k": 3}
    response = requests.post(f"{base_url}/search", json=payload)
    print(f"\nQuery: {query}")
    print(f"Status: {response.status_code}")
    result = response.json()
    if "error" in result:
        print(f"Error: {result['error']}")
    else:
        print(f"Found {len(result.get('results', []))} results")
        for i, res in enumerate(result.get('results', []), 1):
            text = res.get('meta', {}).get('text', 'N/A')
            score = res.get('score', 'N/A')
            print(f"  {i}. {text[:50]}... (Score: {score})")

print("\n" + "=" * 50)
print("API Testing Complete!")
