#!/usr/bin/env python3
"""Calculadora infix.

Funcionamento:

[operação] [n1] [n2]

Operações:
sum -> +
sub -> =
mul -> *
div -> /

Uso:
$ infixcalc.py sum 5 2
7

$ infixcalc.py mul 10 5
50

$ infixcalc.py
operação: sum
n1: 5
n2: 4
9

Os resultados serão salvos em 'infixcalc.log'
"""
__version__ = "0.1.0"
__author__ = "Rafael Schwambach"
__license__ = "Unlicense"

import os
import sys
import logging

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("Rafael", log_level) 
ch = logging.StreamHandler()
ch.setLevel(log_level)
fmt = logging.Formatter(
    "%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s"
)
ch.setFormatter(fmt)
log.addHandler(ch)

from datetime import datetime
arguments = sys.argv[1:]

# Validacao
if not arguments: # Esse If Not é basicamente se o usuário não passar argumentos. Como se fosse um If Isblank
    operation = input("operação:")
    n1 = input("n1:")
    n2 = input("n2:")
    arguments = [operation, n1, n2]

# Validacao
elif len(arguments) != 3:
    print("Número de argumentos inválidos")
    print("ex: 'sum 5 5'")
    sys.exit(1)

operation, *nums = arguments

valid_operations = ("sum", "sub", "mul", "div")
if operation not in valid_operations:
    print("Operação invalida")
    print(valid_operations)
    sys.exit(1)

validated_nums = []
for num in nums:
    # TODO: Repetição while + exceptions
    if not num.replace(".","").isdigit(): #Verificando se o número é valido (isdigit()). Replace no . em null apenas no loop
        print(f"Número inválido: {num}")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    validated_nums.append(num)

try:
    n1, n2 = validated_nums
except ValueError as e:
    print(str(e))

# TODO: usar dict de funcoes
if operation == "sum":
    result = n1 + n2
elif operation == "sub":
    result = n1 - n2
elif operation == "mul":
    result = n1 * n2
elif operation == "div":
    result = n1 / n2

print(f"O resultado é {result}")

path = os.curdir
filepath = os.path.join(path, "infixcalc.log")
timestamp = datetime.now().isoformat()
user = os.getenv('USER','anonymous')

try:
    with open(filepath, "a") as file_:
        file_.write(f"{timestamp} - {user} - {operation}, {n1}, {n2} = {result}\n") 
except PermissionError as e:
    log.error(
        "You don't have permissions to access the file."
        "%s ", str(e)
    )
    print(str(e))
    sys.exit(1)