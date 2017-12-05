import argparse
import api

parser = argparse.ArgumentParser(description='A cli utility for interact with Github.')
parser.add_argument('--user', dest='username', type=str, nargs=1,help='the Github username')
parser.add_argument('command', metavar='cmd', type=str, nargs=1, help='command to run')

args = parser.parse_args()


def main():
    if (args.command[0] == "ls"):
        res = api.list_user_repos(args.username[0])
        print("\n".join(res))
        return
    pass

if __name__ == "__main__":
    main()

