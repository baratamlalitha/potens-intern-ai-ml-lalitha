from app.pdf_reader import load_pdfs
from app.chunking import chunk_text
from app.embeddings import create_embedding
from app.vector_store import add_to_index
from app.retrieval import search
from app.llm import generate_answer

documents = load_pdfs("data/pdfs")

print(f"Loaded {len(documents)} pages")

total_chunks = 0

for doc in documents:

    chunks = chunk_text(doc["text"])

    for chunk in chunks:

        embedding = create_embedding(chunk)

        metadata = {
            "source": doc["source"],
            "page": doc["page"],
            "text": chunk
        }

        add_to_index(embedding, metadata)

        total_chunks += 1

print(f"Stored {total_chunks} chunks in FAISS")

query = "What are the principles of trustworthy AI?"

results = search(query)

answer = generate_answer(query, results)

print("\nANSWER:\n")

print(answer)

print("\nCITATIONS:\n")

for result in results:

    print("=" * 50)

    print(f"Source: {result['source']}")

    print(f"Page: {result['page']}")