import re
import requests
from lxml import html
from libs.variaveis import Cor

def cabecalho(codigo):
    print("""{verde}
        ###################
        #  {padrao}{codigo}{verde}  #
        ###################
    """.format(
            verde=Cor.verde.value,
            padrao=Cor.padrao.value,
            codigo=codigo)
        )

class Correios():

    def __init__(self, codigo):
        cabecalho(codigo)
        self.rastreio(codigo)

    def escape(self, lista):
        text = " ".join(str(item) for item in lista)
        text = text.replace("\r", " ").replace("\t", " ").replace("\xa0", " ").strip()
        return re.sub(' +', ' ', text)

    def rastreio(self, obj):
        s = requests.Session()

        obj_post = {
            'objetos': obj,
            'btnPesq': '+Buscar'
        }

        s.headers.update({
            'Host': 'www2.correios.com.br',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://www2.correios.com.br/sistemas/rastreamento/default.cfm',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Content-Length': '37',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        })
        r = s.post('http://www2.correios.com.br/sistemas/rastreamento/resultado.cfm?', data=obj_post, allow_redirects=True)
        r.encoding = 'ISO-8859-1'

        if r.status_code == 200:
            if r.text.find('listEvent') == -1:
                print(Cor.amarelo.value+'['+Cor.vermelho.value+'#'+Cor.amarelho.value+'] Erro na requisição')
                return None

            tree = html.fromstring(r.text.encode('latin1'))
            trs = tree.xpath('//table[contains(@class,"listEvent")]/tr')

            for tr in trs:
                tds = tr.xpath('./td')

                data = self.escape(tds[0].xpath('./text() | ./label/text()'))
                text = self.escape(tds[1].xpath('./text()'))
                status = tds[1].xpath('./strong/text()')[0]

                print(Cor.amarelo.value + data)
                print(Cor.ciano.value + status)
                print(Cor.padrao.value + text)
                print(Cor.roxo.value + '-'*50 + Cor.padrao.value)
