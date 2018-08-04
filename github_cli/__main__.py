"""GitHub CLI - Command line interface for interact with GitHub
Usage:
  github_cli <command> [<args>...]
  github_cli (-i | --interactive)

Options:
  -h --help     Show this screen.
  --version     Show version.

Available Commands:
  ls            List files in a directory
  cd            Change directory
"""
from sys import argv

from docopt import docopt

from github_cli.github_cmd import GitHubCmd

def main():
    arguments = docopt(__doc__, version='0.0.1', options_first=True)

    cmd = GitHubCmd()
    if arguments['-i'] or arguments['--interactive']:
        cmd.cmdloop()
    else:
        cmd.onecmd(" ".join(argv[1:]))


if __name__ == '__main__':
    main()