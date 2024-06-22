#!/usr/bin/env python
"""Imprime a tabuada do 1 ao 10.

---Tabuada do 1---

     1 x 1 = 1
     2 x 1 = 2
     3 x 1 = 3
...
###################
---Tabuada do 2---

     2 x 1 = 2
     2 x 2 = 4
     2 x 3 = 6
...
###################
"""
__version__ = "0.1.0"
__author__ = "Rafael Schwambach"

#template nao mais utilizado
template = """
---Tabuada do {n1}---

     {bloco}

###################
"""

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Iterable (percorriveis)
numeros = list(range(1, 11))

# para cada numero em numeros:
for n1 in numeros:
    print("{:-^18}".format(f"Tabuada do {n1}"))
    print()
    for n2 in numeros:
        resultado = n1 * n2
        print("{:^18}".format(f"{n1} x {n2} = {resultado}"))
    print("#" * 18)
#bloco += f"{n1} x {n2} = {resultado}\n"
# bloco += significa bloco = bloco + algo
#print(template.format(bloco=bloco, n1 = n1))
# misturando format com f strings.

# A f string é do tipo f"Texto, {variável}"
#A str.format é do tipo 'formatacao'.format(texto):
# "{:^4}.format("oi")"