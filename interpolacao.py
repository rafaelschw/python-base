#!usr/bin/env python
"""Imprime a mensagem de um e-mail

NAO MANDE SPAM!!!
"""

__version__ = "0.1.1"

import sys
import os

arguments = sys.argv[1:]
if not arguments:
     print("Please inform the file name")
     sys.exit(1)

filename = arguments[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path, filename) #emails.txt
templatepath = os.path.join(path,"email_tmpl.txt") # email_tmpl.txt

for line in open(filepath):
    name, email = line.split(",")

     # TODO: Substituir por envio de email
    print(f"Enviando email para: {email}")
    print()
    print(
         open(templatepath).read()
         % {
             "nome": name,
             "produto": "caneta",
             "texto": "Escrever muito bem",
             "link": "https://canetaslegais.com",
             "quantidade": 1,
             "preco": 50.5,
             }
        )
print("-" * 50)