import svn.remote

from github_cli.base.Path import Path
from github_cli.base.Subcommand import Subcommand
from github_cli.utils import _extract_absolute_path


class LsSubcommand(Subcommand):
    """Usage: ls [<dirpath>]"""

    def _execute(self, arg):
        return self.execute_from_dirpath(arg["<dirpath>"])

    def execute_from_dirpath(self, dirpath):
        context_path = self.context.curpath
        absolute_path = _extract_absolute_path(dirpath, context_path)
        print("ls processing ", absolute_path)
        return self._do_ls_absolute_path(absolute_path)

    def _do_ls_absolute_path(self, absolute_path:Path):

        if absolute_path.is_root():
            filename_list = self._do_ls_root()
        elif absolute_path.only_user():
            filename_list = self._do_ls_user_level(absolute_path)
        else:
            filename_list = self._do_ls_fullpath(absolute_path)

        return filename_list

    def _do_ls_root(self):
        for u in self.api_manager.get_users():
            yield u.name

    def _do_ls_fullpath(self, path:Path):
        r = svn.remote.RemoteClient(path.to_remote_address())
        for obj in r.list():
            yield obj

    def _do_ls_user_level(self, path:Path):
        if path.only_user():
            return self._do_ls_only_user(path)
        else:
            return self._do_ls_fullpath(path)

    def _do_ls_only_user(self, path:Path):
        for r in self.api_manager.get_user(path.user_name).get_repos():
            yield r.name

