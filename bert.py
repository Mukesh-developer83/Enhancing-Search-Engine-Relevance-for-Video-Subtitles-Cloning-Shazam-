from sentence_transformers import SentenceTransformer

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
embedding_documents = model.encode([clean_subtitle_text(doc) for doc in subtitle_documents])
