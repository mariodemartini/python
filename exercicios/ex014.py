# DICIONARIOS
# igual listas mas usa indice litral em vez de númericos
# dicionário são identificados por chaves {} ou dict()
# dados={'nome':'Pedro','idade':25}
# print(dados['nome']) - Pedro

# dados['sexo']='M' - cria um novo elemento no dicionário
# del dados['idade'] - elimina o elemento

filme = {'titulo':'Star Wars',
         'ano':1977,
         'diretor':'George Lucas'  
         }
print(filme.values())
# retorna o conteudo/valores
print(filme.keys())
# retorna as chaves/descriminação
print(filme.items())
# retorna as chaves e valores
for k,v in filme.items():
    print(f'O {k} é {v}')
    
# podemos colocar o dicionário dentro da lista
# locadora=('dicionário 1', 'dicionario 02', 'dicionario 03')

pessoas={'nome':'Mario','sexo':'M','idade':34}
pessoas['Kg']= 79.8
# aspas duplas porque no dicionário já fica com aspas simples
print(pessoas.items())
print(pessoas.values())
print(pessoas.keys())
print(f'O {pessoas["nome"]} tem {pessoas["idade"]}')
# no dicionário não tem o for enumerate
del pessoas['Kg']
print(pessoas.keys())
brasil=list()
estado1={'UF':'São Paulo', 'Capital':'São Paulo'}
estado2={'UF':'Minas Gerais', 'Capital':'Belo Horizonte'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0]['Capital'])
print(brasil[1]['UF'])

# no dicionário não tem fatiamento para inclui na lista
# usamos copy
est=dict()
br=list()
for c in range(0,3):
    est['UF']=str(input('Unidade Federativa:'))
    est['Sigla']=str(input('Sigla do Estado:'))
    br.append(est.copy())
print(br)








