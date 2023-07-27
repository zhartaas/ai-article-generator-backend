from app.utils import AppModel
from typing import List
from fastapi import status, HTTPException, Depends
from . import router
from ..service import Service, get_service
from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data


class SelectTopicRequest(AppModel):
    topics: List[str]


class SelectTopicResponse(AppModel):
    topics: List


@router.post(
    "/select_topics",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=SelectTopicResponse,
)
def select_topics(
    userInput: SelectTopicRequest,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> list:
    print("\n\n##################\n\n")
    print(userInput)
    print("\n\n##################\n\n")
    list_of_topics = []
    for topic in userInput.topics:
        list_of_topics.append(topic)

    topics = svc.repository.insert_topics(jwt_data.user_id, list_of_topics)
    return SelectTopicResponse(topics=topics)
