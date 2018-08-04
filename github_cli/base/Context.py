from pathlib import PosixPath

import yaml

from github_cli.base.Path import Path
from github_cli.utils import get_logger, is_valid_token


class Context(object):
    def __init__(self):
        self.curpath = Path("/")
        self.user_name_path = None
        self.repo_name_path = None

        self.token = None
        self.user_name = None

    def is_empty(self):
        return self.user_name_path is None and self.repo_name_path is None

    def only_user(self):
        return self.user_name_path is not None and self.repo_name_path is None

    def is_token_valid(self):
        return self.token is not None

    def update_absolute_path(self, updated_absolute_path):
        self.curpath = updated_absolute_path

    def load_from_yaml(self):
        yaml_obj = yaml.load(open("./config.yml").read())

        self.token = yaml_obj.get("token", None)
        if self.token is None or not is_valid_token(self.token):
            get_logger().warning("Token not properly initialized.")

        self.user_name = yaml_obj.get("username", None)
        if self.user_name is None:
            get_logger().warning("Username not properly initialized.")

    def dump_to_yaml(self):
        open("./config.yml", "w").write(yaml.dump(
            {
                "token": self.token,
                "username": self.user_name
            }))