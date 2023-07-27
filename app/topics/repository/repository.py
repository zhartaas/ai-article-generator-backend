from pymongo.database import Database
from bson.objectid import ObjectId


class TopicsRepository:
    def __init__(self, database: Database):
        self.database = database

    def insert_topics(self, user_id: str, topics: list):
        self.database["topics"].insert_one(
            {"user_id": ObjectId(user_id), "topics": topics}
        )
        self.database["articles"].insert_one({"_id": ObjectId(user_id)})
        return topics

    def get_topics(self, user_id):
        topics = self.database["topics"].find_one({"user_id": ObjectId(user_id)})
        return topics["topics"]
