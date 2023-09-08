from app.utils import AppModel
from fastapi import Depends
from ...articles.router import router
from ...articles.service import Service, get_service
from app.topics.service import Service as TopicsService
from app.topics.service import get_service as topics_get_service
from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data


class GenerateArticleResponse(AppModel):
    article: dict


class GenerateArticleRequest(AppModel):
    topics: str


@router.post("/generate_article", response_model=GenerateArticleResponse)
def generate_article(
    input: GenerateArticleRequest,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
    svc_topics: TopicsService = Depends(topics_get_service),
) -> dict:
    if input.topics:
        topics = input.topics
    else:
        topics_list = svc_topics.repository.get_topics(jwt_data.user_id)
        topics = ", ".join(topics_list)
    article = svc.llm.generate_article(topics)
    svc.repository.insert_article(jwt_data.user_id, article)
    return GenerateArticleResponse(article=article)


3
