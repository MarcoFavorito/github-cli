import sys
import argparse
import cli

# parser = argparse.ArgumentParser(description='A cli utility for interact with Github.')
# parser.add_argument('--user', dest='username', type=str, nargs=1,help='the Github username')
# parser.add_argument('command', metavar='cmd', type=str, nargs=1, help='command to run')
# args = parser.parse_args()


def main():
    command_parser = cli.GithubCmd()
    line = " ".join([x if not " " in x else '"' + x + '"' for x in sys.argv[1:]])
    if len(sys.argv)<2:
        print("Usage: python github-cli.py CMD")
        print("Please type 'python github-cli.py help [CMD]' for further informations")
        sys.exit(1)
    cmd = sys.argv[1].strip()
    if (cmd=="shell"):
        command_parser.cmdloop()
    else:
        res = command_parser.onecmd(line)
        sys.exit(0)
    pass




if __name__ == "__main__":
    main()

