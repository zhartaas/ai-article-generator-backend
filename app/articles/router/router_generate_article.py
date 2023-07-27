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


@router.post("/generate_article", response_model=GenerateArticleResponse)
def generate_article(
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
    svc_topics: TopicsService = Depends(topics_get_service),
) -> dict:
    topics = svc_topics.repository.get_topics(jwt_data.user_id)
    article = svc.llm.generate_article(topics)
    svc.repository.insert_article(jwt_data.user_id, article)
    return GenerateArticleResponse(article=article)
