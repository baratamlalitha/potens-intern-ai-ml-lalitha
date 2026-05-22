import numpy as np

from app.vector_store import index, documents_store
from app.embeddings import create_embedding

def search(query, top_k=3):

    query_embedding = create_embedding(query)

    vector = np.array([query_embedding]).astype('float32')

    distances, indices = index.search(vector, top_k)

    results = []

    for idx in indices[0]:

        results.append(documents_store[idx])

    return results