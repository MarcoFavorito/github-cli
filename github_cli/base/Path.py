from pathlib import PosixPath


class Path(object):
    def __init__(self, path):

        parsed_path = PosixPath(path)
        self.full_path_str = str(parsed_path)
        self.parts = parsed_path.parts
        self.anchor = parsed_path.anchor

        self.shift = 1 if self.anchor else 0

        self.user_name = self.parts[self.shift] if len(self.parts) > self.shift else None
        self.repository_name = self.parts[self.shift+1] if len(self.parts)>self.shift+1 else None

    def depth(self):
        return len(self.parts)-1 if self.is_absolute() else len(self.parts)

    def is_root(self):
        return len(self.parts) == 1

    def only_user(self):
        return self.depth()==1

    def is_absolute(self):
        return self.anchor

    def no_anchor(self):
        shift = 1 if self.anchor else 0
        return Path(self.full_path_str[shift:])

    def to_remote_address(self):
        assert self.user_name and self.repository_name
        subpath = "/".join(self.parts[2+self.shift:])
        return "https://github.com/{}/{}/trunk/{}".format(self.user_name, self.repository_name, subpath)
        
    def __str__(self):
        return self.full_path_str