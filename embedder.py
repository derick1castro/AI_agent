import openai
import numpy as np
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_embedding(text, model="text-embedding-3-small"):
    response = openai.embeddings.create(
        model=model,
        input=text,
    )
    return np.array(response.data[0].embedding)
