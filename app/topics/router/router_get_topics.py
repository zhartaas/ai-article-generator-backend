from app.utils import AppModel
from typing import List
from fastapi import status, HTTPException, Depends
from . import router
from ..service import Service, get_service
from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data


class GetTopicsResponse(AppModel):
    topics: List[str]


@router.get("/get_topics", response_model=GetTopicsResponse)
def get_topics(
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> list:
    topics = svc.repository.get_topics(jwt_data.user_id)
    return GetTopicsResponse(topics=topics)
