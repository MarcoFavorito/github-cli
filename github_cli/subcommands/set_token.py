import getpass

import svn.remote
from github import Github

from github_cli.base.Path import Path
from github_cli.base.Subcommand import Subcommand
from github_cli.utils import _extract_absolute_path, is_valid_token, get_logger
import svn.remote


class SetTokenSubcommand(Subcommand):
    """Usage: set_token <your_github_token> [-u <username>]"""

    def _execute(self, arg):
        input_token = arg["<your_github_token>"]
        input_username = arg.get(["<username>"], self.context.user_name)

        if is_valid_token(input_token):
            self.context.token = input_token
            self.context.user_name = input_username
            self.context.dump_to_yaml()
        else:
            get_logger().error("Token is not valid.")
            return