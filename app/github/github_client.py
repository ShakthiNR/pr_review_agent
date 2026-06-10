import os

from github import Github

github_client = Github(
    os.getenv("GITHUB_TOKEN")
)