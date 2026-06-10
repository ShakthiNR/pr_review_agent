from fastapi import APIRouter, Request

from app.services.diff_service import get_pr_diff
from app.agents.pr_review_agent import review_pr
from app.github.review_poster import post_review

router = APIRouter()


@router.post("/github/webhook")
async def github_webhook(
    request: Request
):

    payload = await request.json()

    action = payload.get("action")

    if action not in [
        "opened",
        "synchronize"
    ]:
        return {
            "message": "ignored"
        }

    repo_name = payload["repository"]["name"]

    owner = payload["repository"]["owner"]["login"]

    pr_number = payload["pull_request"]["number"]

    diff = get_pr_diff(
        owner,
        repo_name,
        pr_number
    )

    review = review_pr(diff)

    post_review(
        owner,
        repo_name,
        pr_number,
        review
    )

    return {
        "message": "review completed"
    }