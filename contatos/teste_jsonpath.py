import requests
import jsonpath

categorias = requests.get('http://127.0.0.1:8000/api/v2/categorias/')
re_categorias = jsonpath.jsonpath(categorias.json(), 'results')

contatos = requests.get('http://127.0.0.1:8000/api/v2/contatos/')
re_contatos = jsonpath.jsonpath(contatos.json(), 'results')
contato = jsonpath.jsonpath(contatos.json(), 'results[0]')
nome = jsonpath.jsonpath(contatos.json(), 'results[0].nome')
sobrenome = jsonpath.jsonpath(contatos.json(), 'results[0].sobrenome')

print(re_categorias)
print()
print(re_contatos)
print()
print(contato)
print()
print(nome)
print()
print(sobrenome)
print()
