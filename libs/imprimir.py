from libs.variaveis import Cor

class Imprimir():

    def __init__(self, rastreio):
        self.cabecalho(rastreio["codigo"])

        if "movimentacoes" in list(rastreio.keys()):
            self.movimentacoes(rastreio["movimentacoes"])
        else:
            self.erro(rastreio["erro"])

    def erro(self, erro):
         print(Cor.amarelo.value+'['+Cor.vermelho.value+'#'+Cor.amarelo.value+'] '+ erro)

    def cabecalho(self, codigo):
        print("""{verde}
            ###################
            #  {padrao}{codigo}{verde}  #
            ###################
        """.format(
                verde=Cor.verde.value,
                padrao=Cor.padrao.value,
                codigo=codigo)
            )

    def movimentacoes(self, lista):
        for movimentacao in lista:
            print(Cor.amarelo.value + movimentacao["data"])
            print(Cor.ciano.value + movimentacao["status"])
            print(Cor.padrao.value + movimentacao["texto"])
            print(Cor.roxo.value + '-'*50 + Cor.padrao.value)
