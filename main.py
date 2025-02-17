from search import search_employees

if __name__ == "__main__":
    
    while True:
        query = input("Enter query (exit for Exit): ").strip()
        if query.lower()=="exit":
            exit(0)
        page = int(input("Enter page number: ").strip())
        results = search_employees(query, page)

        for res in results:
            print(res)
