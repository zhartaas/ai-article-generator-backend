from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
import json

# from dotenv import load_dotenv, find_dotenv

# load_dotenv(find_dotenv)

article_generator_template = """
Your task is to perform the following actions:
1. Randomly pick one topic from list
2. Imagine you are expert in this topic. Generate article related on this topic. Follow the rules of writing articles and make it interesting for people.    
3. Get text from this article
4. Write intriguing introduction on this topic.

Output in JSON format by following schema:
topic: topic
article_name: Article Name
content: Text
"""


class LangChain:
    def __init__(self, key: str):
        self.llm = ChatOpenAI(
            openai_api_key=key,
            model="gpt-3.5-turbo",
        )

    def generate_article(self, topics: list) -> str:
        escaped_template = article_generator_template.replace("\n", "\\n").replace(
            '"', '\\"'
        )

        messages = [
            SystemMessage(content=escaped_template),
            HumanMessage(content=topics),
        ]

        article = json.loads(self.llm(messages=messages).content)

        return article
