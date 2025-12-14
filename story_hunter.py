# # # agents/story_hunter.py
# # import requests

# # API_KEY = "a8d6cb57df674a2b926d54d88fc33cb3"

# # def get_headlines(country="in", limit=5):
# #     """
# #     Fetch top headlines from NewsAPI.
# #     :param country: country code (default = India)
# #     :param limit: number of headlines
# #     :return: list of dicts [{headline, source}]
# #     """
# #     url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}"
# #     res = requests.get(url).json()

# #     headlines = []
# #     for article in res.get("articles", [])[:limit]:
# #         headlines.append({
# #             "headline": article.get("title"),
# #             "source": article.get("source", {}).get("name")
# #         })

# #     return headlines

# # # Quick test
# # if __name__ == "__main__":
# #     for h in get_headlines():
# #         print("📰", h["headline"], "| Source:", h["source"])
# # agents/story_hunter.py - Enhanced version
# import requests
# import os
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# class StoryHunterAgent:
#     def __init__(self):
#         self.api_key = os.getenv("NEWS_API_KEY")
#         self.name = "Story Hunter"
        
#     def get_headlines(self, country="in", limit=5):
#         """
#         Fetch top headlines from NewsAPI.
#         :param country: country code (default = India)
#         :param limit: number of headlines
#         :return: list of dicts [{headline, source, description, url}]
#         """
#         url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={self.api_key}"
        
#         try:
#             res = requests.get(url).json()

#             headlines = []
#             for article in res.get("articles", [])[:limit]:
#                 headlines.append({
#                     "headline": article.get("title"),
#                     "source": article.get("source", {}).get("name"),
#                     "description": article.get("description", "No description"),
#                     "url": article.get("url"),
#                     "published_at": article.get("publishedAt"),
#                     "discovery_time": str(datetime.now()),
#                     "agent": self.name
#                 })

#             return headlines
            
#         except Exception as e:
#             print(f"❌ Story Hunter Error: {e}")
#             return []
    
#     def get_breaking_news(self, query="breaking", limit=5):
#         """Get breaking news by keyword"""
#         url = f"https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&apiKey={self.api_key}"
        
#         try:
#             res = requests.get(url).json()
#             articles = []
            
#             for article in res.get("articles", [])[:limit]:
#                 articles.append({
#                     "headline": article.get("title"),
#                     "source": article.get("source", {}).get("name"),
#                     "description": article.get("description", "No description"),
#                     "url": article.get("url"),
#                     "published_at": article.get("publishedAt"),
#                     "type": "breaking_news",
#                     "agent": self.name
#                 })
            
#             return articles
            
#         except Exception as e:
#             print(f"❌ Breaking News Error: {e}")
#             return []

# # Backward compatibility
# def get_headlines(country="in", limit=5):
#     hunter = StoryHunterAgent()
#     return hunter.get_headlines(country, limit)

# # Quick test
# if __name__ == "__main__":
#     hunter = StoryHunterAgent()
    
#     print("🔍 Testing Story Hunter Agent...")
#     headlines = hunter.get_headlines(limit=3)
    
#     for i, h in enumerate(headlines, 1):
#         print(f"{i}. 📰 {h['headline']}")
#         print(f"   📡 Source: {h['source']}")
#         print(f"   📝 Description: {h['description'][:100]}...")
#         print()
    
#     print("🚨 Testing Breaking News...")
#     breaking = hunter.get_breaking_news(limit=2)
#     for story in breaking:
#         print(f"🔥 {story['headline']}")
#         print(f"   Source: {story['source']}")
#         print()
import requests
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class StoryHunterAgent:
    def __init__(self):
        self.api_key = os.getenv("GNEWS_API_KEY")
        if not self.api_key:
            raise ValueError("GNEWS_API_KEY not found in environment variables")
        self.name = "Story Hunter"
        
    def get_headlines(self, country="in", limit=5):
        """Fetch top headlines from GNews API"""
        url = "https://gnews.io/api/v4/top-headlines"
        params = {
            "country": country,
            "lang": "en",
            "max": limit,
            "token": self.api_key
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            
            headlines = []
            for article in data.get("articles", [])[:limit]:
                headlines.append({
                    "headline": article.get("title"),
                    "source": article.get("source", {}).get("name"),
                    "description": article.get("description", "No description"),
                    "url": article.get("url"),
                    "published_at": article.get("publishedAt"),
                    "discovery_time": datetime.now().isoformat(),
                    "agent": self.name
                })
            
            return headlines
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Story Hunter Error: {str(e)}")
            return []

# ...existing code...
    
    def get_breaking_news(self, query="breaking", limit=5):
        """
        Get breaking news by keyword
        Args:
            query (str): Search query
            limit (int): Number of articles
        Returns:
            list: List of breaking news articles
        """
        url = "https://gnews.io/api/v4/top-headlines"
        params = {
           "country": "in",
           "lang": "en",
           "max": 5,
           "token": "GNEWS_API_KEY"
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            res = response.json()
            
            return [{
                "headline": article.get("title"),
                "source": article.get("source", {}).get("name"),
                "description": article.get("description", "No description"),
                "url": article.get("url"),
                "published_at": article.get("publishedAt"),
                "type": "breaking_news",
                "agent": self.name
            } for article in res.get("articles", [])[:limit]]
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Breaking News Error: {str(e)}")
            return []

# Backward compatibility
def get_headlines(country="in", limit=5):
    hunter = StoryHunterAgent()
    return hunter.get_headlines(country, limit)

if __name__ == "__main__":
    hunter = StoryHunterAgent()
    
    print("🔍 Testing Story Hunter Agent...")
    headlines = hunter.get_headlines(limit=3)
    
    for i, h in enumerate(headlines, 1):
        print(f"{i}. 📰 {h['headline']}")
        print(f"   📡 Source: {h['source']}")
        print(f"   📝 Description: {h['description'][:100]}...")
        print()
    
    print("🚨 Testing Breaking News...")
    breaking = hunter.get_breaking_news(limit=2)
    for story in breaking:
        print(f"🔥 {story['headline']}")
        print(f"   Source: {story['source']}")
        print()