from fastapi import FastAPI
from app.api.webhook import router

app = FastAPI()

app.include_router(router)

@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "service": "github-pr-review-agent"
    }