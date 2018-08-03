from abc import ABC, abstractmethod

from docopt import docopt, DocoptExit
from github import Github

from github_cli.base.Context import Context


# def docopt_cmd(func):
#     """
#     This decorator is used to simplify the try/except block and pass the result
#     of the docopt parsing to the called action.
#     """
#     def fn(self, arg):
#         try:
#             opt = docopt(fn.__doc__, arg)
#
#         except DocoptExit as e:
#             # The DocoptExit is thrown when the args do not match.
#             # We print a message to the user and the usage block.
#
#             print('Invalid Command!')
#             print(e)
#             return
#
#         except SystemExit:
#             # The SystemExit exception prints the usage for --help
#             # We do not need to do the print here.
#
#             return
#
#         res = func(self, opt)
#         print()
#         return res
#
#     fn.__name__ = func.__name__
#     fn.__doc__ = func.__doc__
#     fn.__dict__.update(func.__dict__)
#     return fn

def doc_command(doc):
    def decorator(func):
        def wrapper(self, arg):
            return func(self, arg)

        wrapper.__doc__ = doc
        return wrapper
    return decorator



class Subcommand(ABC):

    def __init__(self, github_api_manager:Github, context:Context):
        self.api_manager = github_api_manager
        self.context = context

    def execute(self, arg):
        try:
            opt = docopt(self.__doc__, arg)
            res = self._execute(opt)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return res

    @abstractmethod
    def _execute(self, arg):
        raise NotImplementedError


