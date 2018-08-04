import cmd
from github import Github

from github_cli.base.Context import Context
from github_cli.base.Subcommand import doc_command
from github_cli.subcommands.cd import CdSubcommand
from github_cli.subcommands.cp import CpSubcommand
from github_cli.subcommands.get_token import GetTokenSubcommand
from github_cli.subcommands.ls import LsSubcommand
from github_cli.subcommands.mkdir import MkdirSubcommand
from github_cli.subcommands.rmdir import RmdirSubcommand
from github_cli.subcommands.set_token import SetTokenSubcommand
from github_cli.utils import ask_password


class GitHubCmd(cmd.Cmd):
    intro = 'Welcome to GitHub-CLI!' \
        + ' (type help for a list of commands.)'
    prompt = '$ '
    file = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.context = Context()
        self.context.load_from_yaml()

        self.api_manager = self._setup_api_manager()
        self.prompt = str(self.context.curpath) + '$ '

    def _setup_api_manager(self):
        if self.context.is_token_valid():
            api_manager = Github(self.context.token)
        else:
            username = input("Username: ")
            password = ask_password()
            api_manager = Github(username, password)

        return api_manager

    @doc_command(LsSubcommand.__doc__)
    def do_ls(self, arg):
        filename_list = LsSubcommand(self.api_manager, self.context).execute(arg)
        for filename in filename_list:
            print(filename)

    @doc_command(CdSubcommand.__doc__)
    def do_cd(self, arg):
        updated_absolute_path = CdSubcommand(self.api_manager, self.context).execute(arg)
        if updated_absolute_path:
            self.context.update_absolute_path(updated_absolute_path)
            self.prompt = str(updated_absolute_path) + "$ "

    @doc_command(MkdirSubcommand.__doc__)
    def do_mkdir(self, arg):
        MkdirSubcommand(self.api_manager, self.context).execute(arg)

    @doc_command(RmdirSubcommand.__doc__)
    def do_rmdir(self, arg):
        RmdirSubcommand(self.api_manager, self.context).execute(arg)

    @doc_command(CpSubcommand.__doc__)
    def do_cp(self, arg):
        CpSubcommand(self.api_manager, self.context).execute(arg)

    @doc_command(SetTokenSubcommand.__doc__)
    def do_set_token(self, arg):
        SetTokenSubcommand(self.api_manager, self.context).execute(arg)

    @doc_command(GetTokenSubcommand.__doc__)
    def do_get_token(self, arg):
        token, username = GetTokenSubcommand(self.api_manager, self.context).execute(arg)
        print("Token: {}\nUsername: {}".format(token, username))

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""
        print('Quitting...')
        exit()