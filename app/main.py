from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.auth.router import router as auth_router
from app.topics.router import router as topics_router
from app.articles.router import router as articles_router
from app.config import client, env, fastapi_config

app = FastAPI(**fastapi_config)


@app.on_event("shutdown")
def shutdown_db_client():
    client.close()

                        
origins = ["*"]  # Allow requests from any origin

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allow all HTTP headers
)

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(topics_router, prefix="/topics", tags=["Topics"])
app.include_router(articles_router, prefix="/articles", tags=["Articles"])
