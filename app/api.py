from fastapi import FastAPI
from pydantic import BaseModel
from app.translation import (
    translate_to_english,
    translate_to_original_language
)
from app.pdf_reader import load_pdfs
from app.chunking import chunk_text
from app.embeddings import create_embedding
from app.vector_store import add_to_index
from app.retrieval import search
from app.llm import generate_answer
from deep_translator import GoogleTranslator
from app.contradiction import check_contradiction

app = FastAPI()

documents = load_pdfs("data/pdfs")

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


class QueryRequest(BaseModel):
    query: str


@app.get("/")
def home():

    return {
        "message": "RAG API Running"
    }


@app.post("/ask")
def ask_question(request: QueryRequest):

    translated_query = translate_to_english(
        request.query
    )

    results = search(translated_query)

    answer = generate_answer(
        translated_query,
        results
    )

    if any(ord(char) > 128 for char in request.query):
        final_answer = translate_to_original_language(
             answer,
             "te"
        )
    else:
        final_answer = answer
    citations = []

    for result in results:

        citations.append({
            "source": result["source"],
            "page": result["page"]
        })

    return {
        "query": request.query,
        "answer": final_answer,
        "citations": citations
    }

@app.post("/check-contradiction")
def contradiction_checker(request: QueryRequest):

    results = search(request.query)

    if len(results) < 2:

        return {
            "message": "Not enough related documents found."
        }

    text1 = results[0]["text"]

    text2 = results[1]["text"]

    analysis = check_contradiction(
        text1,
        text2
    )

    return {
        "query": request.query,
        "analysis": analysis,
        "source_1": {
            "source": results[0]["source"],
            "page": results[0]["page"]
        },
        "source_2": {
            "source": results[1]["source"],
            "page": results[1]["page"]
        }
    }