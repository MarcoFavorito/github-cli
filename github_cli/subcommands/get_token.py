import getpass

import svn.remote
from github import Github

from github_cli.base.Path import Path
from github_cli.base.Subcommand import Subcommand
from github_cli.utils import _extract_absolute_path
import svn.remote


class GetTokenSubcommand(Subcommand):
    """Usage: get_token"""

    def _execute(self, arg):
        return self.context.token, self.context.user_name