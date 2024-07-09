"""
Alerta de temperatura

Faça um script que pergunta ao usuário qual a temperatura atual e o índice de umidade do ar,
sendo que caso será exibida uma mensagem de alerta dependendo das condições:

temp maior 45: ALERTA!!! Perigo calor extremo
temp vezes 3 for maior ou igual a umidade: ALERTA!!! Perigo de calor úmido
temp entre 10 e 30: Normal
temp entre 0 e 10: Frio
temp <0: ALERTA: Frio extremo
"""
import sys
import logging
log = logging.Logger("alerta")

# TODO: Usar funções para ler input

info  = {
    "temperatura": None,
    "umidade": None
}

while True:
# Condição de parada
# O dicionário está completamente preenchido
    info_size = len(info.values())
    filled_size = len([value for value in info.values() if value is not None])
    if info_size == filled_size:
        break # para o while

    for key in info.keys(): # ["temperatura", "umidade"]
        if info[key] is not None:
            continue
        try:
            info[key] = int(input(f"Qual é a {key}? ").strip())
        except ValueError:
            log.error("%s inválida, digite números", key)
            break # para o for

temp, umid = info.values() # unpacking


if temp > 45:
    print(f"ALERTA!!!  Perigo calor extremo. Temp: {temp}")
elif temp > 30 and temp*3 >= umid:
    print(f"ALERTA!!! Perigo de calor úmido. Temp: {temp}. Umid: {umid}")
elif temp >= 10 and temp <= 30:
    print(f"Normal. Temp: {temp}") 
elif temp >= 0 and temp <= 10:
    print(f"Frio. temp: {temp}")
elif temp < 0:
    print(f"ALERTA: Frio extremo; Temp: {temp}. Umid: {umid}")