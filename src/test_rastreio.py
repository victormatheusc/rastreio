import pytest
from rastreio import Track17, Correios

codigos_test = {
    "RF955476774CN": {'movimentacoes': [{'texto': '', 'data': '09/11/2017 15:52 PARNAMIRIM / RN', 'status': 'Objeto entregue ao destinatário'}, {'texto': '', 'data': '09/11/2017 07:29 PARNAMIRIM / RN', 'status': 'Objeto saiu para entrega ao destinatário'}, {'texto': 'de CENTRO INTERNACIONAL em CURITIBA / PR para Unidade Operacional em Liberado sem imposto. Entrega em 40 dias / BR', 'data': '13/10/2017 09:13 CURITIBA / PR', 'status': 'Objeto encaminhado'}, {'texto': '', 'data': '06/10/2017 18:37 CURITIBA / PR', 'status': 'Objeto recebido pelos Correios do Brasil'}, {'texto': '', 'data': '23/09/2017 11:24 CHINA / CN', 'status': 'Objeto postado'}], 'codigo': 'RF955476774CN'}
}

def test_correios():
    for codigo in codigos_test:
        assert Correios.rastrear(codigo) == codigos_test[codigo]
