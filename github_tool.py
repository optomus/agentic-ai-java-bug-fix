# github_tool.py
from github import Github

class GitHubTool:
    def __init__(self, token):
        self.client = Github(token)

    def get_file_content(self, repo_name, file_path, branch="main"):
        repo = self.client.get_repo(repo_name)
        contents = repo.get_contents(file_path, ref=branch)
        return contents.decoded_content.decode()

    def create_pr(self, repo_name, title, body, branch, filename, new_content):
        repo = self.client.get_repo(repo_name)
        source = repo.get_branch("main")
        repo.create_git_ref(ref=f"refs/heads/{branch}", sha=source.commit.sha)
        contents = repo.get_contents(filename, ref="main")
        repo.update_file(contents.path, title, new_content, contents.sha, branch=branch)
        pr = repo.create_pull(title=title, body=body, head=branch, base="main")
        return pr.html_url
