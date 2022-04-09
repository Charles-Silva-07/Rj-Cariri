from django.test import Client


def test_status_code(client:Client):
    resp = client.get('/') # fizemos uma chamada do tipo get logo na raiz da aplicação
    assert resp.status_code == 200 # nos certificamos que o retorno e igual ao 200
