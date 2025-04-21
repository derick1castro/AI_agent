import json
import faiss
import numpy as np
from embedder import get_embedding
from tqdm import tqdm

class Retriever:
    def __init__(self, data_path):
        self.data = self._load_data(data_path)
        self.index, self.id_map = self._build_index(self.data)

    def _load_data(self, path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def _build_index(self, data):
        embeddings = []
        id_map = []

        print("Embedding documents...")
        for item in tqdm(data):
            embedding = get_embedding(item['text'])
            embeddings.append(embedding)
            id_map.append(item)

        dim = len(embeddings[0])
        index = faiss.IndexFlatL2(dim)
        index.add(np.array(embeddings).astype("float32"))

        return index, id_map

    def search(self, query, k=2):
        query_embedding = get_embedding(query).astype("float32").reshape(1, -1)
        D, I = self.index.search(query_embedding, k)
        return [self.id_map[i]["text"] for i in I[0]]
