#!/usr/bin/env python

import os
import sys
import subprocess

# Function to handle the cd command
def cd_command(directory):
    try:
        if not directory:
            print(os.getcwd())
        else:
            os.chdir(directory)
            os.environ['PWD'] = os.getcwd()
    except FileNotFoundError:
        print("Directory not found")

# Function to clear the screen
def clr_command():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')

# Function to list contents of a directory
def dir_command(directory):
    try:
        if not directory:
            directory = os.getcwd()
        contents = os.listdir(directory)
        print("\n".join(contents))
    except FileNotFoundError:
        print("Directory not found")

# Function to list environment strings
def environ_command():
    for key, value in os.environ.items():
        print(key + '=' + value)

# Function to display a comment
def echo_command(comment):
    print(comment)

# Function to display help
def help_command():
    with open('user_manual.txt', 'r') as manual:
        print(manual.read())

# Function to pause shell operation
def pause_command():
    input("Press Enter to continue...")

# Function to create a directory
def mkdir_command(directory):
    try:
        os.makedirs(directory)
        print("Directory created successfully")
    except FileExistsError:
        print("Directory already exists")

# Function to remove a directory
def rmdir_command(directory):
    try:
        os.rmdir(directory)
        print("Directory removed successfully")
    except FileNotFoundError:
        print("Directory not found")
    except OSError as e:
        print(f"Error: {e}")

# Function to create a text file
def create_file(filename):
    try:
        with open(filename, 'w') as file:
            print("File '{}' created successfully.".format(filename))
    except Exception as e:
        print("Error creating file:", e)

# Function to edit a text file
def edit_file(filename):
    try:
        if sys.platform.startswith('win'):
            os.system('notepad ' + filename)
        else:
            os.system('nano ' + filename)
    except Exception as e:
        print("Error editing file:", e)

# Function to remove a text file
def remove_file(filename):
    try:
        os.remove(filename)
        print("File '{}' removed successfully.".format(filename))
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("Error removing file:", e)

# Main shell loop
def shell():
    while True:
        command = input("$ ")
        if not command:
            continue
        elif command == "clr":
            clr_command()
        elif command.split()[0] == "cd":
            cd_command(command.split()[1] if len(command.split()) > 1 else None)
        elif command.split()[0] == "dir" or command.split()[0] == "ls":
            dir_command(command.split()[1] if len(command.split()) > 1 else None)
        elif command == "environ":
            environ_command()
        elif command.split()[0] == "echo":
            echo_command(" ".join(command.split()[1:]))
        elif command == "help":
            help_command()
        elif command == "pause":
            pause_command()
        elif command.split()[0] == "mkdir":
            mkdir_command(command.split()[1] if len(command.split()) > 1 else None)
        elif command.split()[0] == "rmdir":
            rmdir_command(command.split()[1] if len(command.split()) > 1 else None)
        elif command.startswith("create"):
            create_file(command.split()[1] if len(command.split()) > 1 else None)
        elif command.startswith("edit"):
            edit_file(command.split()[1] if len(command.split()) > 1 else None)
        elif command.startswith("remove") or command.startswith("rm"):
            remove_file(command.split()[1] if len(command.split()) > 1 else None)
        elif command == "quit" or command == "exit":
            break
        else:
            subprocess.run(command.split())

# Check if command line argument is provided for batch file
if len(sys.argv) > 1:
    try:
        with open(sys.argv[1], 'r') as batch_file:
            for line in batch_file:
                subprocess.run(line.strip().split())
    except FileNotFoundError:
        print("Batch file not found")
else:
    shell()
