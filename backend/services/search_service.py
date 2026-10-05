class SearchService:
    def search(self, query: str):
        return [{"title": "Example Result", "link": "http://example.com", "snippet": "Example snippet"}]

search_service = SearchService()
