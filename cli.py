import cmd
import api
import argparse
import shlex
import utils as u

class GithubCmd(cmd.Cmd):

    def do_help(self, arg):
        'List available commands with "help" or detailed help with "help cmd".'
        super(GithubCmd, self).do_help(arg)

    def do_ls(self, line):
        """ls USERNAME      List public repositories of the user with `username`."""
        parser = argparse.ArgumentParser(prog="ls")
        parser.add_argument('username', type=str, help='the Github username')

        args = parser.parse_args(shlex.split(line.strip()))

        json_res = api.get_users_repos(args.username)
        repos_full_names = [x["full_name"] for x in json_res]
        print("\n".join(repos_full_names))

    def do_mkdir(self, line):
        """mkdir --user username --name repo_name [--desc description] [--private]      """
        parser = argparse.ArgumentParser(prog="mkdir")
        parser.add_argument('username',    type=str, help='the Github username')
        parser.add_argument('name',        type=str, help='the new repo name')
        parser.add_argument('--desc', dest='description', type=str, help='the repo description', default="")
        parser.add_argument('--private', dest='private',
                            action='store_const',
                            const=True, default=False, help='use this flag if you want a private repo')

        args = parser.parse_args(shlex.split(line.strip()))

        u.get_logger().info(args)

        data = {
            "name"          :args.name,
            "description"   :args.description,
            "private"       :args.private,

        }

        res = api.post_user_repos(args.username, data)
        print(res)

    def do_rmdir(self, line):
        """rmdir [--user username] [--name repo_name]
        """
        parser = argparse.ArgumentParser(prog="rmdir")
        parser.add_argument('username', type=str, help='the Github username')
        parser.add_argument('name', type=str, help='the new repo name')

        args = parser.parse_args(shlex.split(line.strip()))

        res = api.delete_user_repo(args.username, args.name)


    # def do_EOF(self, line):
    #     return True

    def do_quit(self, line):
        """quit     exit the shell.
        """
        return True

