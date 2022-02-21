import requests


class TestCategorias:
    headers = {'Authorization': 'Token e9d48e25f87ec1703b2627ab5237c4d12610e63d'}
    url_base_categorias = 'http://127.0.0.1:8000/api/v2/categorias/'

    def test_get_categorias(self):
        categorias = requests.get(url=self.url_base_categorias, headers=self.headers)
        assert categorias.status_code == 200

    def test_get_categoria(self):
        categoria = requests.get(url=f'{self.url_base_categorias}1/', headers=self.headers)
        assert categoria.status_code == 200

    def test_post_categoria(self):
        novo = {
            'nome': 'AIAI'
        }

        resultado = requests.post(url=self.url_base_categorias, headers=self.headers, data=novo)
        assert resultado.status_code == 200 and resultado.json()['nome'] == novo['nome']

    def test_put_categoria(self):
        atualizado = {
            'nome': 'Coleguinha'
        }
        resposta = requests.get(url=f'{self.url_base_categorias}4/', headers=self.headers, data=atualizado)
        assert resposta.status_code == 200 and resposta.json()['nome'] == atualizado['nome']

    def test_delete_categoria(self):
        resposta = requests.delete(url=f'{self.url_base_categorias}12/', headers=self.headers)
        assert resposta.status_code == 204 and len(resposta.text) == 0
