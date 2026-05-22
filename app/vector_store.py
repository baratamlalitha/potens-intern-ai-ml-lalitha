import faiss
import numpy as np

dimension = 384

index = faiss.IndexFlatL2(dimension)

documents_store = []

def add_to_index(embedding, metadata):

    vector = np.array([embedding]).astype('float32')

    index.add(vector)

    documents_store.append(metadata)