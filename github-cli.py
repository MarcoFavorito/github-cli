import argparse
import cli

parser = argparse.ArgumentParser(description='A cli utility for interact with Github.')
parser.add_argument('--user', dest='username', type=str, nargs=1,help='the Github username')
parser.add_argument('command', metavar='cmd', type=str, nargs=1, help='command to run')

args = parser.parse_args()


def main():
    command_parser = cli.GithubCmd()
    cmd = args.command[0]
    if (cmd=="shell"):
        command_parser.cmdloop()
    elif (hasattr(command_parser, "do_" + cmd)):
        function_to_call = getattr(command_parser, "do_"+cmd)
        res = function_to_call(args.username[0])
        print("\n".join(res))
        return
    pass




if __name__ == "__main__":
    main()

