from langchain_huggingface import HuggingFaceEmbeddings
embedding = HuggingFaceEmbeddings(model = "sentence-transformers/all-MiniLM-L6-v2")

# text = "Hello how are you? "
document = [
    "Hello how are you",
    "What are you doing"
]
vectors = embedding.embed_documents(document)
print(vectors)