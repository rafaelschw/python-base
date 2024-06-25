#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala que
frequentam cada uma das atividades.
"""
__version__ = "0.1.1"

from pprint import pprint

# Dados
sala1 = {
    "nomes" : ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
}
sala2 = {
    "nomes" : ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]
}

aula_ingles = {
    "nomes" : ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
}
aula_musica = {
    "nomes" : ["Erik", "Carlos", "Maria"]
}
aula_danca = {
    "nomes" : ["Gustavo", "Sofia", "Joana", "Antonio"]
}

atividades = {
    "Inglês" : aula_ingles,
    "Música" : aula_musica,
    "Dança" : aula_danca
}

for atividade in atividades:
    print(f"Alunos da atividade {atividade}\n")
    
    atividade_sala1 = set(sala1['nomes']) & set(atividades[atividade]['nomes'])
    atividade_sala2 = set(sala2['nomes']) & set(atividades[atividade]['nomes'])

    print(f"Sala 1: ", atividade_sala1)
    print(f"Sala 2: ", atividade_sala2)
    

# # Listar alunos em cada atividade por sala

# for atividade in atividades:

#     print(f"Alunos da atividade {atividade[""]}\n")

# # Criando os conjuntos e realizando as interseções

#     atividade_sala1 = set(sala1) & set(atividade)
#     atividade_sala2 = set(sala2).intersection(set(atividade))

#     print(f"Sala 1: ", atividade_sala1)
#     print(f"Sala 2: ", atividade_sala2)
    
#     print()
#     print("#" * 50)
