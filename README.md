# Github-cli

A command line utility for interact with Github.

It is under development. Use it at your own risk.

Any contribution/suggestion would be really welcome.

## How to use
Clone this repository:

    git clone https://github.com/MarcoFavorito/github-cli.git
        
Call `github_cli` from the root directory:

    cd github-cli 
    python github_cli.py -i            # to run the interactive shell 
    python github_cli.py <command> ... # to run a single command
    
It is recommended to configure `.config.yml` with `username` and `token` variables ([guide about how to generate a personal token](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/)).

## Examples

- run the shell:

      python github_cli.py -i
      
You can also run single commands without starting a shell.
   
- run the `help`:

      $ help [cmd]
        
- list public repositories of an user (`ls`):
        
      $ ls Your_Username
   
  list files under a repository or a subdirectory:
  
      $ ls Your_Username/Your_Repository/subfolder

- create your repo:

      $ mkdir Your_Username/hello-world
        
- remove a repo

       $ rmdir Your_Username/hello-world
       
- copy files/folders in the local filesystem:

       $ cp Your_Username/hello-world/subdirectory ./hello-world/local_subdirectory

## License
The software is released under MIT license. 