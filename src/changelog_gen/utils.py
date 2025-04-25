import os
from github import Github

def get_github_token():
    token = os.getenv('GITHUB_TOKEN')
    if not token:
        raise RuntimeError("GITHUB_TOKEN environment variable not set.")
    return token

def create_release(tag, token, draft=True):
    """Create or update a GitHub Release for the given tag."""
    repo_name = os.getenv('GITHUB_REPOSITORY')
    if not repo_name:
        raise RuntimeError("GITHUB_REPOSITORY environment variable not 
set.")
    gh = Github(token)
    repo = gh.get_repo(repo_name)
    # 读取 CHANGELOG.md 中对应 tag 段落
    body = ""
    lines = []
    try:
        with open('CHANGELOG.md', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        pass
    start = None
    header = f"## [{tag}]\n"
    for i, line in enumerate(lines):
        if line == header:
            start = i
            break
    if start is not None:
        for line in lines[start+1:]:
            if line.startswith("## ["):
                break
            body += line

    # 创建或更新 release
    try:
        release = repo.get_release(tag)
        release.update_release(name=tag, message=body, draft=draft)
    except:
        repo.create_git_release(tag, tag, body, draft=draft)

