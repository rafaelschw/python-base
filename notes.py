#!/user/bin/env python3
"""Bloco de notas

$ notes.py new "Minha Nota"
tag: tech
text: 
Anotação Geral sobre carreira de tecnologia

$ notes.py read tech
...
...

$ notes.py search text
Return all messages that contain the referred text.
"""
__version__ = "0.1.0"

import os
import sys

cmds = ("read", "new", "search")
path = os.curdir
filepath = os.path.join(path,"notes.txt")

arguments = sys.argv[1:]
if not arguments:
    print("Invalid usage")
    print(f"You must specify a subcommand {cmds}")
    sys.exit(1)

if arguments[0] not in cmds:
    print(f"Invalid command {arguments[0]}")
    print(f"The valid commands are: {cmds}")

try:
    teste = arguments[1]
except IndexError as e:
    print(f"{str(e)}")
    print("You must insert additional information")
    sys.exit(1)

if arguments[0] == "read":
    # Leitura das notas
    for line in open(filepath):
        title, tag, text = line.split("\t")
        if tag.lower() == arguments[1].lower():
            print(f"title: {title}")
            print(f"text: {text}")
            print("-" * 30)
            print()

if arguments[0] =="new":
    try:
        title = arguments[1] # TODO: Tratar exception
    except IndexError as e:
        print(f"{str(e)}")
        print("You must insert the note title")
        print("example: $ notes.py new 'Title'")
        sys.exit(1)
    text = [
        f"{title}",
        input("tag:").strip(),
        input("text:\n").strip(),
    ]
    # \t - tsv (tab separated values)
    with open(filepath, "a") as file_:
        file_.write("\t".join(text) + "\n")

if arguments[0] == "search":
    # Leitura dos texts das notas
    for line in open(filepath):
        title, tag, text = line.split("\t")
        if  arguments[1].lower() in text.lower():
            print(f"title: {title}")
            print(f"text: {text}")
            print("-" * 30)
            print()