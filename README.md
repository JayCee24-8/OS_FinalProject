# JYShell: A Simple Unix-Like Shell

## Overview

JYShell is a command-line shell developed for an Operating Systems course project. It provides core functionalities found in Unix-like shells and supports internal commands, external program execution, input/output redirection, and batch file execution.

This project demonstrates the principles of process management, input/output handling, and command parsing in operating systems.

## Features

### Internal Commands
- **`cd <directory>`**: Change the current working directory. Displays the current directory if none is specified.
- **`clr`**: Clears the terminal screen.
- **`dir <directory>`**: Lists contents of the specified or current directory.
- **`environ`**: Displays all environment variables.
- **`echo <comment>`**: Outputs the provided comment.
- **`help`**: Displays the user manual.
- **`pause`**: Pauses shell operations until Enter is pressed.
- **`quit`**: Exits JYShell.

### Additional Commands
- **`mkdir <directory>`**: Creates a new directory.
- **`rmdir <directory>`**: Removes an empty directory.
- **`create <filename>`**: Creates a new text file.
- **`edit <filename>`**: Opens the specified text file for editing using the default text editor.
- **`remove <filename>`** or **`rm <filename>`**: Deletes the specified text file.

### Program Execution
JYShell can execute external programs by typing their name followed by arguments. The programs run as child processes of the shell.

### Input/Output Redirection
Supports redirection for commands using:
- `<` for input
- `>` for output

Example:
```bash
programname arg1 arg2 < inputfile > outputfile
