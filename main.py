import sys
from libs.rastreio import Correios
from libs.imprimir import Imprimir

def main():
    argumentos = [codigo for codigo in sys.argv[1:]]
    if argumentos:
        codigos = argumentos
    else:
        print("Digite o(s) codigo(s) a ser(em) rastreado(s) [OBS: Separados por espaço somente]: ", end="")
        codigos = [item for item in input().strip().split(" ")]

    for codigo in codigos:
        Imprimir(Correios.rastrear(codigo))

if __name__ == '__main__':
    main()
