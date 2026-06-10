from app.github.github_client import github_client


def get_pr_diff(owner, repo_name, pr_number):

    repo = github_client.get_repo(
        f"{owner}/{repo_name}"
    )
    pr = repo.get_pull(pr_number)
    diff_text = ""

    for file in pr.get_files():
        diff_text += f"\nFILE: {file.filename}\n"
        if file.patch:
            diff_text += file.patch

    return diff_text