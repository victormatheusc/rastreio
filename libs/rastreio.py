import re
import requests
from lxml import html

class Correios():
    def rastrear(obj):
        def escape(lista):
            texto = " ".join(str(item) for item in lista)
            texto = texto.replace("\r", " ").replace("\t", " ").replace("\xa0", " ").strip()
            return re.sub(' +', ' ', texto)

        sessao = requests.Session()
        obj_post = {
            'objetos': obj,
            'btnPesq': '+Buscar'
        }
        sessao.headers.update({
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
        req = sessao.post('http://www2.correios.com.br/sistemas/rastreamento/resultado.cfm?', data=obj_post, allow_redirects=True)
        req.encoding = 'ISO-8859-1'
        retorno = {"codigo": obj}
        if req.status_code == 200:
            if req.text.find('listEvent') == -1:
                erro = "Erro na requisição"
                retorno["erro"] = erro
                print("[#] " + erro)
                return retorno

            tree = html.fromstring(req.text.encode('latin1'))
            trs = tree.xpath('//table[contains(@class,"listEvent")]/tr')

            movimentacoes = []
            for tr in trs:
                tds = tr.xpath('./td')

                movimentacoes.append(
                    {
                        "data": escape(tds[0].xpath('./text() | ./label/text()')),
                        "status": tds[1].xpath('./strong/text()')[0],
                        "texto": escape(tds[1].xpath('./text()'))
                    }
                )

            retorno["movimentacoes"] = movimentacoes
            return retorno

        else:
            erro = "Erro ao verificar as movimentações"
            retorno["erro"] = erro
            print("[#] " + erro)
            return retorno
