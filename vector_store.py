# from qdrant_client import QdrantClient
# from qdrant_client.models import Distance, VectorParams
# from database import get_pg_connection
# from embeddings import generate_embedding
# from qdrant_client.models import PointStruct

# client = QdrantClient("localhost", port=6333)

# COLLECTION_NAME = "employee_skills"

# def setup_qdrant():
#     client.recreate_collection(
#         collection_name=COLLECTION_NAME,
#         vectors_config=VectorParams(size=384, distance=Distance.COSINE)  # Adjust based on embedding size
#     )



# def index_bios():
#     conn = get_pg_connection()
#     cursor = conn.cursor()
#     cursor.execute("SELECT user_id, bio FROM skills")

#     points = []
#     for user_id, bio in cursor.fetchall():
#         vector = generate_embedding(bio)
#         points.append(PointStruct(id=user_id, vector=vector, payload={"user_id": user_id, "bio": bio}))

#     client.upsert(collection_name=COLLECTION_NAME, points=points)
#     conn.close()


from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from database import get_pg_connection
from embeddings import generate_embedding
import os
from dotenv import load_dotenv

load_dotenv()

QDRANT_HOST = os.getenv("QDRANT_HOST", "localhost")
QDRANT_PORT = int(os.getenv("QDRANT_PORT", 6333))
COLLECTION_NAME = "employee_skills"

client = QdrantClient(QDRANT_HOST, port=QDRANT_PORT)

def setup_qdrant():
    client.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(size=384, distance=Distance.COSINE)  # Adjust vector size
    )

def index_bios():
    conn = get_pg_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT user_id, bio FROM skills")

    points = []
    for user_id, bio in cursor.fetchall():
        bio_lower = bio.lower()  # Convert bio to lowercase
        vector = generate_embedding(bio_lower)
        points.append({
            "id": user_id,
            "vector": vector,
            "payload": {"user_id": user_id, "bio": bio_lower}  # Store lowercase bio
        })

    client.upsert(collection_name=COLLECTION_NAME, points=points)
    conn.close()
    print("Qdrant database populated successfully.")

if __name__ == "__main__":
    setup_qdrant()
    index_bios()


