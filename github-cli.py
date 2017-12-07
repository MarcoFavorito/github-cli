import sys
import argparse
import cli

# parser = argparse.ArgumentParser(description='A cli utility for interact with Github.')
# parser.add_argument('--user', dest='username', type=str, nargs=1,help='the Github username')
# parser.add_argument('command', metavar='cmd', type=str, nargs=1, help='command to run')
#
# args = parser.parse_args()


def main():
    command_parser = cli.GithubCmd()
    cmd = sys.argv[1].strip()
    if (cmd=="shell"):
        command_parser.cmdloop()
    # elif (hasattr(command_parser, "do_" + cmd)):
    else:
        line = " ".join(sys.argv[1:])
        res = command_parser.onecmd(line)
        if res: print(res)
        return
    pass




if __name__ == "__main__":
    main()

