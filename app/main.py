from fastapi import FastAPI
from app.routes.review import router

app = FastAPI(title="CodeReview AI")
app.include_router(router, prefix="/api")