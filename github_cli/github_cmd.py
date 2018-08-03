import cmd


from github import Github

from github_cli.base.Context import Context
from github_cli.base.Subcommand import doc_command
from github_cli.subcommands.cd import CdSubcommand
from github_cli.subcommands.ls import LsSubcommand


class GitHubCmd(cmd.Cmd):
    intro = 'Welcome to GitHub-CLI!' \
        + ' (type help for a list of commands.)'
    prompt = '$ '
    file = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.api_man = Github()
        self.context = Context()
        self.prompt = str(self.context.curpath) + '$ '

    @doc_command(LsSubcommand.__doc__)
    def do_ls(self, arg):
        filename_list = LsSubcommand(self.api_man, self.context).execute(arg)
        for filename in filename_list:
            print(filename)

    @doc_command(CdSubcommand.__doc__)
    def do_cd(self, arg):
        updated_absolute_path = CdSubcommand(self.api_man, self.context).execute(arg)
        if updated_absolute_path:
            self.prompt = str(updated_absolute_path) + "$ "
            self.context.curpath = updated_absolute_path

    def do_cp(self, arg):
        pass

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""
        print('Quitting...')
        exit()