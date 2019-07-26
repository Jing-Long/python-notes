% is just used as a comment symbol in this note, it has nothing to do with bash syntax!
chmod +x file_name  % make this file executable
Files start with #! (called hashbang) in first line and have been made executable can be run with ./file_name directly.
Simple command:[ variable=value ... ] command name [ command arguments ... ] [ redirection operations... ] 
               % = means variable assignments, [] means optional, ... means can be repeated many times.
Pipelines: [time [-p]] [ ! ] command1 [ [|||&] command2 ... ]
           % keyword time is used to find out how long it takes to run our commands
           % command 1 and 2 will run simultaneously
           % "pipe" symbol | tells bash to connect the output of the first to the input of the second command. 
           % symbol |& inbetween the commands to indicate that we want not only the standard output of the first command,
             but also its standard error to be connected to the second command's input. This is usually undesirable. 
Lists: A list is a sequence of commands. In essence, a script is a command list. Commands in lists are separated by
       a control operator which tells bash what to do when executing the command before it. 
       command control-operator [ command2 control-operator ... ]
       1. control operator ; starts a new line and tells bash to just run the command and wait for it to end before
          advancing to the next command in the list. 
       2. control operator || tells bash to run the command before it as it normally would, but after finishing that command 
          moves to the next command only if the command before it failed. If the command before it didn't fail, the ||
          operator will make bash skip the command after it. This is useful for showing error messages when a command fails. 
