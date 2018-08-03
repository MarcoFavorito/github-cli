# Github-cli

A command line utility for interact with Github.

It is under development. Use it at your own risk.

Any contribution/suggestion would be really welcome.

## Examples

- run the shell:

      python github_cli.py
      
You can also run single commands without starting a shell.
   
- run the `help`:

      $ help [cmd]
        
- list public repositories of an user (`ls`):
        
      $ ls Your_Username
   
  list files under a repository or a subdirectory:
  
      $ ls Your_Username/Your_Repository/subfolder

## To be implemented
- create your repo:

      $ mkdir Your_Username hello-world --desc "hello world!" --private
        
then, an interactive session asks you the password.

- remove a repo

       $ rmdir Your_Username hello-world
       
- copy files/folders in the local filesystem:

       $ cp Your_Username/hello-world/README.md ./hello-world-readme.md

## License
The software is released under MIT license. 