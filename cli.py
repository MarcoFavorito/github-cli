import cmd
import api


COMMANDS = {
    # "ls" : api.list_user_repos,
#    "mkdir": api.create_user_repo
}



class GithubCmd(cmd.Cmd):

    def do_ls(self, username):
        """
        ls username
        List public repositories of the user with `username`.
        """
        if not username:
            self.default("")
        else:
            json_res = api.get_users_repos(username)
            repos_full_names = [x["full_name"] for x in json_res]
            print("\n".join(repos_full_names))

    def do_mkdir(self, username = "", name = "", description = "", is_private = False):
        json_post = {}
        # username, name, description, is_private = line.strip().split()
        if not username:
            username = input("username:")
        if not name:
            json_post["name"] = input("repository name:")
        if not description:
            json_post["description"] = input("description:")
        if not is_private:
            is_private = input("is private? [y/N]:")
            json_post["private"] = True if is_private.lower()=="y" else False
            json_post["private"] = str(json_post["private"]).lower()

        print(json_post)
        res = api.post_user_repos(username, json_post)
        print(res)

    def do_rmdir(self, username = "", name = ""):
        if not username:
            username = input("username:")
        if not name:
            name = input("repository name:")
        res = api.delete_user_repo(username, name)


    def do_EOF(self, line):
        return True

    def do_quit(self, line):
        """
        quit
        exit the shell.
        """
        return True

