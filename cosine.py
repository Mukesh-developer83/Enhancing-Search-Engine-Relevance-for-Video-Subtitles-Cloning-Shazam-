from sklearn.metrics.pairwise import cosine_similarity

# Calculate cosine similarity between query and all document embeddings
cosine_similarities = cosine_similarity(query_embedding, embedding_documents)

# Retrieve the most similar document based on the highest cosine similarity
most_similar_idx = cosine_similarities.argmax()
