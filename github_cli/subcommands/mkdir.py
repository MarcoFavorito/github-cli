import getpass

from github import Github

from github_cli.base.Path import Path
from github_cli.base.Subcommand import Subcommand
from github_cli.utils import ask_password, get_logger


class NoSuchFileOrDirectoryError(Exception):
    def __init__(self, path:Path):
        super().__init__("cd: {}: No such file or directory".format(path.full_path_str))

class NotDirectoryError(Exception):
    def __init__(self, path:Path):
        super().__init__("cd: {}: Not a directory".format(path.full_path_str))

class MkdirSubcommand(Subcommand):
    """Usage: mkdir <repo_full_path>"""

    def _execute(self, arg):
        repository_path = Path(arg["<repo_full_path>"])
        if not repository_path.is_absolute() or repository_path.depth() < 2:
            get_logger().error("Repo path must be of the form '/<username>/<repo_name>'")
            return

        input_username = repository_path.user_name
        input_repository_name = repository_path.repository_name

        if input_username == self.context.user_name:
            self._do_mkdir_from_repository_name_with_context(input_repository_name)
        else:
            self._do_mkdir_from_repository_name_no_context(input_repository_name, input_username)


    def _do_mkdir_from_repository_name_with_context(self, repository_name):
        try:
            if self.context.token is not None:
                temp_api_manager = Github(self.context.token)
            else:
                password = ask_password()
                temp_api_manager = Github(self.context.user_name, password)

            user = temp_api_manager.get_user()
            user.create_repo(repository_name)
        except Exception as e:
            print(e, type(e))
            print("mkdir: Cannot create repo: %s" % repository_name)

    def _do_mkdir_from_repository_name_no_context(self, repository_name, username):
        password = ask_password()
        temp_api_manager = Github(username, password)
        user = temp_api_manager.get_user()
        user.create_repo(repository_name)
