pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': '22', 'fone': 123}
print(pessoas['nome'])
del pessoas['fone']
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('-=' * 50)
# Cópia de dicionário = pessoas.copy()
