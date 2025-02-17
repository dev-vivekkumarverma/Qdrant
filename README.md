# Qdrant

## **Qdrant + PostgreSQL Employee Search System 🚀**  
A Python-based **vector search system** using **Qdrant** and **PostgreSQL** to find employees with specific skills using **natural language queries**.  

---

### **🚀 Features**
✅ **Stores employee bios** in PostgreSQL  
✅ **Converts bios into vector embeddings** using `sentence-transformers`  
✅ **Stores embeddings in Qdrant** for fast similarity search  
✅ **Supports case-insensitive keyword matching**  
✅ **Returns paginated search results**  

---

### **📂 Project Structure**
```
qdrant_search_project/
│── embeddings.py          # Generate vector embeddings
│── database.py            # PostgreSQL connection setup
│── vector_store.py        # Store and search vectors in Qdrant
│── search.py              # Query function for similarity search
│── main.py                # Run queries from command line
│── run.sh                 # Automate setup and execution
│── requirements.txt       # Dependencies
│── docker-compose.yml     # Runs PostgreSQL & Qdrant in containers
│── .env                   # Database credentials
│── README.md              # Documentation
│── init-db.sql            # Creates database, user, and table
```

---

### **📦 Setup**
#### **1️⃣ Clone the Repository**
```sh
git clone git@github.com:dev-vivekkumarverma/Qdrant.git
cd Qdrant
```

#### **2️⃣ Configure Environment Variables**
Create a **`.env`** file:
```ini
POSTGRES_USER=test_user
POSTGRES_PASSWORD=test@123
POSTGRES_DB=test_db
POSTGRES_PORT=5432
QDRANT_HOST=localhost
QDRANT_PORT=6333
```

#### **3️⃣ Run Everything with a Single Command**
```sh
./run.sh
```

This script will:  
✅ **Start Docker containers** (PostgreSQL & Qdrant)  
<!-- ✅ **Create a virtual environment**   -->
✅ **Install dependencies**  
✅ **Populate Qdrant with employee bios**  
✅ **Launch the query system**  

---

### **🔍 Query Example**
```sh
python main.py
```
Example input:
```
Enter query: Databricks SQL
Enter page number: 1
```
Example output:
```json
[
    {
        "user_id": 1,
        "bio": "Experienced data engineer skilled in Databricks, SQL, and Apache Spark.",
        "similarity_score": 0.92,
        "keywords_matched": ["databricks", "sql"]
    },
    {
        "user_id": 6,
        "bio": "Data scientist with strong skills in SQL, Databricks, and Python.",
        "similarity_score": 0.89,
        "keywords_matched": ["databricks", "sql"]
    }
]
```

---

### **🛑 Stopping Everything**
To stop all services:
```sh
docker-compose down
```
To remove all stored data:
```sh
docker-compose down -v
```

---
