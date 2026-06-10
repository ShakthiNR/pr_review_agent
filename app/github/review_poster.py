from app.github.github_client import github_client


def post_review(
        owner,
        repo_name,
        pr_number,
        review_text
):

    repo = github_client.get_repo(
        f"{owner}/{repo_name}"
    )

    pr = repo.get_pull(pr_number)

    pr.create_issue_comment(review_text)