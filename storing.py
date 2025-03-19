import chromadb

# Initialize the ChromaDB database
client = chromadb.Client()
collection = client.create_collection("subtitle_embeddings")

# Store the embeddings with associated metadata
for idx, embedding in enumerate(embedding_documents):
    collection.add(documents=[subtitle_documents[idx]], embeddings=[embedding])
