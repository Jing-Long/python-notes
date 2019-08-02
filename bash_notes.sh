% is just used as a comment symbol in this note, it has nothing to do with bash syntax!

man [command] % bring up the manual page of a program/command to learn about 
                possible command-line options for shell program(s)

echo $PATH % shows the system path where bash to search for the command name you type in. 
echo $SHELL % gives /bin/bash, it means the file bash is the Bash program that starts a Bash shell.
~ % a shortcut to access home directory, can use echo $HOME to find the home directory
.file_name % means this file is hidden. 
ls -a % can list all files and directories, including hidden ones.

add PS1=’\u@\h:\w>’ to .bashrc % change the Bash console prompt style to username@hostname:current_directory>
add test -s ~/.alias && . ~/.alias to .bashrc % check whether file .alias exists, if so, run it. This step ensures that
                                                the content of .alias is read and added to the Bash environment. 
add in .alias: alias ls='ls --color=auto $OPTIONS' % enable colourised output according to their types, eg. file, folder,etc.
               alias ll='ls -colorlh $OPTIONS' % defines a new command alias called ll, which calls ls with the additional 
                                                 options -l for long-listing (more details) 
                                                 and -h for human-readable file size output.
ls -l % gives a list which begins with file type and permissions.
        -rwxrwxrwx % means this is a file, Owner, Group and Other can read(r), write(w) and execute(x) it.
        drwxr--r-- % means this is a directory, Group and Other can only read(r) but not write(-) or execute(-) it. 
     
source .bashrc or restart Bash or open a new Bash shell to activate changes to .bashrc and .alias

rsync % this is a program to copy and synchronise files between computers
gnuplot % this is a plotting package
ssh % connect to another computer.
ssh -X or -Y % forward graphical windows from the connected computer to my local machine through the SSH connection.      

type arguments % describes how arguments would be interpreted if used as command names.
type -a command % prints  all of the places that contain an executable command. This includes aliases and functions.

script start with #! (called hashbang) in first line and have been made executable can be run with ./file_name directly.
                  chmod +x file_name  % make this file executable
                  % script example: #!/usr/bin/env bash
                                    code and command
rm % remove 
cp % copy
blank space(space or tab) can be used to separate multiple arguments.
Escaping is putting a \ character in front of the character tells that we want to make literal. Not recommended.
Quoting is wrapping " " or ' ' characters around the text that we want to make literal. Recommended. Be cautious!
        % use "double quotes" for any argument that contains expansions, such as $variable or $(command) expansions.
        % use 'single quotes' for any other arguments. 
        Single quotes make sure that everything in the quotes remains literal
        while double quotes still allow some bash syntax such as expansions.

file descriptors: standard input (FD 0), standard output (FD 1) and standard error (FD 2).
operator x>file % write FD x to file, it is defaulted to write FD 1 (standard output) to the file if x is not specified.
         2>file % specifically redirect FD2 (standard error) to the file.
         x<file % read FD x from file, it is defaulted to read FD 0 (standard input) from the file if x is not specified.
         >& % prefix it with the file descriptor we want to change 
             and follow it with the file descriptor whose stream we need to "copy".
         x>&y % Make FD x write to FD y's stream.
         x<&y % Make FD x read from FD y's stream.
         Example: 2>&1 means Make FD 2 write(>) to where FD(&) 1 is currently writing.
         &>file % the same as >file 2>&1, make both FD 1 (standard output) and FD 2 (standard error) write to file.
         x>>file % Make FD x append to the end of file.
         &>>file % Append both FD 1 (standard output) and FD 2 (standard error) to the end of file.
         % > empties the file's contents when it opens the file so that only your bytes will be in the file.
           >> keeps the file's existing contents and your stream's bytes are added to the end of it.
/dev/null % a special directory for device files. Device files are special files that represent devices in our system. 

            The null device is a special device that is always empty. Anything you write to it will be lost and nothing
            can be read from it. That makes it a very useful device for discarding information. 
            We stream our unwanted error message to the null device and it disappears.

Simple command:[ variable=value ... ] command name [ command arguments ... ] [ redirection operations... ] 
               % = means variable assignments, [] means optional, ... means can be repeated many times.
               
Pipelines: [time [-p]] [ ! ] command1 [ [|||&] command2 ... ]
           % keyword time is used to find out how long it takes to run our commands
           % command 1 and 2 will run simultaneously
           % "pipe" symbol | tells bash to connect the output of the first to the input of the second command. 
           % symbol |& inbetween the commands to indicate that we want not only the standard output of the first command,
             but also its standard error to be connected to the input of the second command. This is usually undesirable. 
             
Lists: A list is a sequence of commands. In essence, a script is a command list. Commands in lists are separated by
       a control operator which tells bash what to do when executing the command before it. 
       command control-operator [ command2 control-operator ... ]
       1. control operator ; starts a new line and tells bash to just run the command and wait for it to end before
          advancing to the next command in the list. 
       2. control operator || tells bash to run the command before it as it normally would, but after finishing that command 
          moves to the next command only if the command before it failed. If the command before it did not fail, the operator
          || will make bash skip the command after it. This is useful for showing error messages when a command fails. 
          
Compound commands: commands with special syntax inside them. They can behave as a single command in a command list. 
                   if list [ ;|<newline> ] then list [ ;|<newline> ] fi
                   { list ; } % compound commands are included in the {}, they are connected by control operators ; or ||.
                   
Coprocesses: coproc [ name ] command [ redirection ... ]

Functions: group a list of commands under a custom name when need to repeat the same task more than once in your script.
           self-defined_function_name () compound-command [ redirection ]
           % The parentheses () should always be empty. They simply denote the fact that you are declaring a function.



