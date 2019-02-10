from abc import ABC, abstractmethod
from pathlib import PosixPath
from github import Github

import yaml

from github_cli.utils import get_logger, is_valid_token

from pathlib import PosixPath

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
        


class Path(object):
    def __init__(self, path):

        parsed_path = PosixPath(path)
        self.full_path_str = str(parsed_path)
        self.parts = parsed_path.parts
        self.anchor = parsed_path.anchor

        self.shift = 1 if self.anchor else 0

        self.user_name = self.parts[self.shift] if len(self.parts) > self.shift else None
        self.repository_name = self.parts[self.shift+1] if len(self.parts)>self.shift+1 else None

    def depth(self):
        return len(self.parts)-1 if self.is_absolute() else len(self.parts)

    def is_root(self):
        return len(self.parts) == 1

    def only_user(self):
        return self.depth()==1

    def is_absolute(self):
        return self.anchor

    def no_anchor(self):
        shift = 1 if self.anchor else 0
        return Path(self.full_path_str[shift:])

    def to_remote_address(self):
        assert self.user_name and self.repository_name
        subpath = "/".join(self.parts[2+self.shift:])
        return "https://github.com/{}/{}/trunk/{}".format(self.user_name, self.repository_name, subpath)
        
    def __str__(self):
        return self.full_path_str
        


# def docopt_cmd(func):
#     """
#     This decorator is used to simplify the try/except block and pass the result
#     of the docopt parsing to the called action.
#     """
#     def fn(self, arg):
#         try:
#             opt = docopt(fn.__doc__, arg)
#
#         except DocoptExit as e:
#             # The DocoptExit is thrown when the args do not match.
#             # We print a message to the user and the usage block.
#
#             print('Invalid Command!')
#             print(e)
#             return
#
#         except SystemExit:
#             # The SystemExit exception prints the usage for --help
#             # We do not need to do the print here.
#
#             return
#
#         res = func(self, opt)
#         print()
#         return res
#
#     fn.__name__ = func.__name__
#     fn.__doc__ = func.__doc__
#     fn.__dict__.update(func.__dict__)
#     return fn

def doc_command(doc):
    def decorator(func):
        def wrapper(self, arg):
            return func(self, arg)

        wrapper.__doc__ = doc
        return wrapper
    return decorator



class Subcommand(ABC):

    def __init__(self, github_api_manager:Github, context:Context):
        self.api_manager = github_api_manager
        self.context = context

    def execute(self, arg):
        try:
            opt = docopt(self.__doc__, arg)
            res = self._execute(opt)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return res

    @abstractmethod
    def _execute(self, arg):
        raise NotImplementedError


