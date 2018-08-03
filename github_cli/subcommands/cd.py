import svn.remote
from github import Github

from github_cli.base.Path import Path
from github_cli.base.Subcommand import Subcommand
from github_cli.utils import _extract_absolute_path
import svn.remote

class NoSuchFileOrDirectoryError(Exception):
    def __init__(self, path:Path):
        super().__init__("cd: {}: No such file or directory".format(path.full_path_str))

class NotDirectoryError(Exception):
    def __init__(self, path:Path):
        super().__init__("cd: {}: Not a directory".format(path.full_path_str))

class CdSubcommand(Subcommand):
    """Usage: cd <dirpath>"""

    def _execute(self, arg):
        input_path_string = arg["<dirpath>"]
        context_path = self.context.curpath
        absolute_path = _extract_absolute_path(input_path_string, context_path)
        print("cd processing ", absolute_path)
        return self._do_cd_absolute_path(absolute_path)

    def _do_cd_absolute_path(self, absolute_path):
        if absolute_path.only_user():
            path = self._do_cd_user(absolute_path)
        else:
            path = self._do_cd_fullpath(absolute_path)
        return path

    def _do_cd_user(self, path:Path):
        try:
            self.api_manager.get_user(path.user_name)
            return path
        except:
            raise NoSuchFileOrDirectoryError(path)

    def _do_cd_fullpath(self, absolute_path:Path):
        try:
            file_info = svn.remote.RemoteClient(absolute_path.to_remote_address()).info()
            if not file_info["entry_kind"] == "dir":
                raise NotADirectoryError(absolute_path)

        except Exception as e:
            raise NoSuchFileOrDirectoryError(absolute_path)

        return absolute_path

