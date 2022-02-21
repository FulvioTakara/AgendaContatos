import requests

# GET categorias
categorias = requests.get('http://127.0.0.1:8000/api/v2/categorias/')
print(categorias.status_code)
print(categorias.json())

# GET contatos
contatos = requests.get('http://127.0.0.1:8000/api/v2/contatos/')
print(contatos.status_code)
print(contatos.json())
print()
print(contatos.json()['next'])
print()
print(contatos.json()['results'][2])
print()
print(contatos.json()['results'][2]['nome'])
print()
contato = requests.get('http://127.0.0.1:8000/api/v2/contatos/7/')
print(contato.status_code)
print(contato.json())
print()
