import os
import shutil

import svn.remote

from github_cli.core import Path
from github_cli.core import Subcommand
from github_cli.utils import _extract_absolute_path

from pathlib import Path as OSPath

class CpSubcommand(Subcommand):
    """Usage: cp <remote_path> <local_path>

Notice: works only with remote directories."""

    def _execute(self, arg):
        remote_path = Path(arg["<remote_path>"])
        local_path = OSPath(arg["<local_path>"]).absolute()

        cwd = os.getcwd()
        shutil.rmtree("/tmp/github-cli-tmp", ignore_errors=True)
        os.mkdir("/tmp/github-cli-tmp")
        os.chdir("/tmp/github-cli-tmp")

        context_path = self.context.curpath
        absolute_path = _extract_absolute_path(remote_path.full_path_str, context_path)

        remote_client = svn.remote.RemoteClient(absolute_path.to_remote_address())
        remote_client.checkout(absolute_path.to_remote_address())

        shutil.move(absolute_path.parts[-1], str(local_path))

        os.chdir(cwd)
