from github_cli.base.Path import Path


class Context(object):
    def __init__(self, curpath=Path("/"), user_name=None, repo_name=None):
        self.curpath = curpath
        self.user_name = user_name
        self.repo_name = repo_name

    def is_empty(self):
        return self.user_name is None and self.repo_name is None

    def only_user(self):
        return self.user_name is not None and self.repo_name is None
