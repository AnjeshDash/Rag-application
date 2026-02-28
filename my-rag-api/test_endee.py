from endee import Endee, Precision

# Initialize Endee client
client = Endee()
INDEX_NAME = "test_index"

print("Available precision values:")
print([attr for attr in dir(Precision) if not attr.startswith('_')])

print("\nCreating index...")
try:
    client.create_index(
        name=INDEX_NAME,
        dimension=384,
        space_type="cosine",
        precision="float32"
    )
    print("Index created successfully!")
except Exception as e:
    print(f"Error creating index: {e}")

print("\nTesting index list...")
try:
    indexes = client.list_indexes()
    print(f"Available indexes: {indexes}")
except Exception as e:
    print(f"Error listing indexes: {e}")
