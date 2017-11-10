from enum import Enum

class Cor(Enum):
    padrao = "\033[0;0m"
    vermelho = "\033[0;31m"
    verde = "\033[0;32m"
    amarelo = "\033[1;33m"
    ciano = "\033[0;36m"
    roxo = "\033[0;35m"
