from qdrant_client.models import ScoredPoint
from vector_store import client, COLLECTION_NAME
from embeddings import generate_embedding

def search_employees(query: str, page: int = 1, page_size: int = 10):
    query_lower = query.lower()  # Convert query to lowercase
    vector = generate_embedding(query_lower)

    search_result = client.search(
        collection_name=COLLECTION_NAME,
        query_vector=vector,
        limit=page_size,
        offset=(page - 1) * page_size
    )
    employees = []
    for hit in search_result:
        user_id = hit.payload["user_id"]
        bio = hit.payload["bio"]
        matched_keywords = [word for word in query_lower.split() if word in bio]

        employees.append({
            "user_id": user_id,
            "bio": bio,
            "similarity_score": hit.score,
            "keywords_matched": matched_keywords
        })

    # Sort results in descending order of similarity_score
    employees.sort(key=lambda x: x["similarity_score"], reverse=True)

    return employees
