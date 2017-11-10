import sys
from libs.rastreio import Correios

def main(codigos):
    for codigo in codigos:
        Correios(codigo)

if __name__ == '__main__':
    argumentos = [codigo for codigo in sys.argv[1:]]
    if argumentos:
        main(argumentos)
    else:
        print("Digite o(s) codigo(s) a ser(em) rastreado(s) [OBS: Separados por espaço somente]: ", end="")
        codigos = [item for item in input().strip().split(" ")]
        main(codigos)
