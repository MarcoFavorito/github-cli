from github import Github

from github_cli.core import Path
from github_cli.core import Subcommand
from github_cli.utils import ask_password, get_logger


class RmdirSubcommand(Subcommand):
    """Usage: rmdir <repo_full_path>"""

    def _execute(self, arg):
        repository_path = Path(arg["<repo_full_path>"])
        if not repository_path.is_absolute() or repository_path.depth()<2:
            get_logger().error("Repo path must be of the form '/<username>/<repo_name>'")
            return

        input_username = repository_path.user_name
        input_repository_name = repository_path.repository_name
        if input_username == self.context.user_name:
            self._do_rmdir_from_repository_name_with_context(input_repository_name)
        else:
            self._do_rmdir_from_repository_name_no_context(input_repository_name, input_username)


    def _do_rmdir_from_repository_name_with_context(self, repository_name):
        if self.context.token is not None:
            temp_api_manager = Github(self.context.token)
        else:
            password = ask_password()
            temp_api_manager = Github(self.context.user_name, password)

        self._repo_delete(temp_api_manager, self.context.user_name, repository_name)

    def _do_rmdir_from_repository_name_no_context(self, repository_name, username):
        password = ask_password()
        temp_api_manager = Github(username, password)
        self._repo_delete(temp_api_manager, username, repository_name)

    def _repo_delete(self, api_manager, username, repository_name):
        repo = api_manager.get_repo("{}/{}".format(username, repository_name))
        check = input("Are you sure? [N/y]")
        if check=="y":
            repo.delete()
