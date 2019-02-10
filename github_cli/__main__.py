# -*- coding utf-8 -*-

from sys import argv

import argparse
from github_cli.github_cmd import GitHubCmd

parser = argparse.ArgumentParser(prog="github-cli", add_help=True)

def main():
    arguments = parser.parse_args() 
    cmd = GitHubCmd()
    cmd.cmdloop()
#     cmd.onecmd(" ".join(argv[1:]))

if __name__ == '__main__':
    main()

