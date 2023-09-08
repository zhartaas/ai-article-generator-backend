from pymongo.database import Database
from bson.objectid import ObjectId
from datetime import datetime


class ArticleRepository:
    def __init__(self, database: Database):
        self.database = database

    def insert_article(self, user_id: str, article: dict):
        article["created_date"] = datetime.utcnow()
        self.database["articles"].update_one(
            filter={"_id": ObjectId(user_id)}, update=({"$push": {"articles": article}})
        )
        print(article)

    def get_articles(self, user_id) -> list:
        articles_collection = self.database["articles"].find_one(
            {"_id": ObjectId(user_id)}
        )
        articles = articles_collection["articles"]
        # print(type(articles))
        return articles
