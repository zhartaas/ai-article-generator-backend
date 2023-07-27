from app.utils import AppModel
from fastapi import Depends
from typing import List
from ...articles.router import router
from ...articles.service import Service, get_service
from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data


class GetArticlesResponse(AppModel):
    articles: list


@router.get("/get_articles", response_model=GetArticlesResponse)
def get_articles(
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
):
    articles = svc.repository.get_articles(jwt_data.user_id)
    return GetArticlesResponse(articles=articles)
