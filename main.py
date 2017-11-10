import re
import sys
import requests
from lxml import html

R = '\033[0;31m' # red
G = '\033[0;32m' # green
Y = '\033[1;33m' # yellow
C = '\033[0;36m' # cyan
P = '\033[0;35m' # purple
D = '\033[0;0m'  # default

def escape(lista):
    text = " ".join(str(item) for item in lista)
    text = text.replace("\r", " ").replace("\t", " ").replace("\xa0", " ").strip()
    return re.sub(' +', ' ', text)

def rastreio(obj):
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
            print(Y+'['+R+'#'+Y+'] Erro na requisição')
            return None

        tree = html.fromstring(r.text.encode('latin1'))
        trs = tree.xpath('//table[contains(@class,"listEvent")]/tr')

        for tr in trs:
            tds = tr.xpath('./td')

            data = escape(tds[0].xpath('./text() | ./label/text()'))
            text = escape(tds[1].xpath('./text()'))
            status = tds[1].xpath('./strong/text()')[0]

            print(Y + data)
            print(C + status)
            print(D + text)
            print(P + '--------------------------------------------------' + D)

def cabecalho(cod):
    print(G+'''
        ###################
        #  %s%s%s  #
        ###################
    ''' % (D,cod,G))

def main(codigos):
    for codigo in codigos:
        cabecalho(codigo)
        rastreio(codigo)

if __name__ == '__main__':
    # parser = argparse.ArgumentParser(
    #     prog='rastreio',
    #     usage='%(prog)s <codigo[,codigo2,codigo3]>',
    #     description='Rastreio dos correios'
    # )
    #
    # parser.add_argument("c", metavar="cod", type=str, help="word to rotate")
    # args = parser.parse_args()
    # codigos = [cod for cod in args.c.split(',') if len(cod) == 13]
    argumentos = [codigo for codigo in sys.argv[1:]]
    if argumentos:
        main(argumentos)
    else:
        print("Digite o(s) codigo(s) a ser(em) rastreado(s) [OBS: Separados por espaço somente]: ", end="")
        codigos = [item for item in input().strip().split(" ")]
        main(codigos)
