"""Algoritmos

Sequencia de instruções lógicas que visam obter a solução de um problema.

Problemas, Premissas.

Exemplo de ver se é dia de semana, feriado, natal. Se está chovendo, frio, calor, nevando.
Se tem pão integral, baguete.
Para ir à padaria.
"""

# Pseudo código #

import ir, pegar, pedir, tem, comer, ficar

# Premissas
today = "Segunda"
hora = 15
natal = False
chovendo = True
frio = True
nevando = True
semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
feriado = ["Quarta"]
horario_padaria = {
    "semana": 19,
    "fds": 12
}

# Algoritmo
if today in feriado and not natal:
    padaria_aberta = False
elif today not in semana and hora < horario_padaria["fds"]:
    padaria_aberta = True
elif today in semana and hora < horario_padaria["semana"]:
    padaria_aberta= True
else:
    padaria_aberta = False

if padaria_aberta:
    if chovendo and (frio or nevando):
        pegar("guarda-chuva")
        pegar("blusa")
        pegar("botas")
    elif chovendo and not frio:
        pegar("guarda-chuva")
        pegar("garrafa de água")
    elif chovendo:
        pegar("guarda-chuva")

    ir("padaria")

    if tem("pao integral") and tem("baguete"):
        pedir(6, "pao integral")
        pedir(6, "baguete")
    elif tem("pao integral") or tem("baguete"):
        pedir(12, "qualquer um dos dois")
    else:
        pedir(6, "qualquer pao")
else:
    ficar("casa")
    comer("bolacha")