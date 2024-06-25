#!/usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da língua configurada no ambiente, o programa exibe a mensagem 
correspondente.

Usage:

Tenha a variável LANG devidamente configurada. Ex.:

    export LANG=pt_BR

Ou informe atraves do CLI argument '--lang'

Ou o usuário terá que digitar.

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.1.3"
__author__ = "Rafael Schwambach"
__license__ = "Unlicense"

import os
import sys

# Definição de quais argumentos o programa aceita receber

arguments = {"lang": None, "count": 1}

for arg in sys.argv[1:]:
    # TODO: Tratar ValueError
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid Option '{key}'")
        sys.exit()
    arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
    # TODO: Usar repetição
    if "LANG" in os.environ:
        current_language =  os.getenv("LANG")
    else:
        current_language = input("Choose a language: ")

current_language = current_language[:5]

msg = {
    "en_US" : "Hello, World!",
    "pt_BR" : "Olá, Mundo!",
    "it_IT" : "Ciao, Mondo!",
    "fr_FR" : "Bonjour, Monde!",
    "es_ES" : "Hola, Mundo!",
}

# Ordem Complexidade O(n)
# if current_language == "pt_BR":
#     msg = "Olá, Mundo!"
# elif current_language == "pt_IT":
#     msg = "Ciao, Mondo!"
# elif current_language == "es_SP":
#     msg = "Hola, Mundo!"
# elif current_language == "fr_FR":
#     msg = "Bonjour, Monde!"

# O(1) - constante
print(
    msg[current_language] * int(arguments["count"])
) 