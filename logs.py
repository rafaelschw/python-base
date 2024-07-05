#!/usr/bin/env python3
"""
Criando logs de errors.

# Criação da nossa instancia de log (bem complexo. Ver documentação de logging)
log = logging.Logger("Rafael", log_level) # poderia ser __name__. Def tbm nivel de log q vai aparecer
# Definição do level que iremos mostrar usando Handler
ch = logging.StreamHandler() # Console/terminal/stderr
ch.setLevel(log_level)
# formatacao - Hr atual; Nome do logger; level name; n da linha; nome do arquivo; mensagem
fmt = logging.Formatter(
    "%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s"
)
ch.setFormatter(fmt)
# destino
log.addHandler(ch)

São 10 linhas que usaremos em todos os códigos.
Quando usa muito uma série de códigos: BOILERPLATE

- Para trocar o arquivo onde queremos salvar o log, basta trocar o StreamHandler()
necessário from logging import handlers
e substituir o ch por fh
"""

import os
import logging
from logging import handlers

# BOILERPLATE
# TODO: usar função
# TODO: usar lib (loguru)
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("Rafael", log_level) 
# ch = logging.StreamHandler()
# ch.setLevel(log_level)
fh = handlers.RotatingFileHandler(
    "meulog.log", 
    maxBytes=100, # Recomendado usar 10**6
    backupCount=10,
)
fh.setLevel(log_level)
fmt = logging.Formatter(
    "%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s"
)
# ch.setFormatter(fmt)
fh.setFormatter(fmt)
log.addHandler(fh)

"""
log.debug("Mensagem pro dev, qe, sysadmin")
log.info("Mensagem geral para usuarios")
log.warning("Aviso que não causa erro")
log.error("Erro que afeta uma unica execucao")
log.critical("Erro geral ex: banco de dados sumiu")
"""

try:
    1/0
except ZeroDivisionError as e:
    log.error("Deu erro %s", str(e))
    # stderr