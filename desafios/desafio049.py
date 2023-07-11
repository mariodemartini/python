print('JOGO DE DADOS')
print('='*35)
from random import randint
from time import sleep
from operator import itemgetter
jogo={'jogador1': randint(1,6),
      'jogador2': randint(1,6),
      'jogador3': randint(1,6),
      'jogador4': randint(1,6)}
ranking=list()
print('Valores sorteados:')
for k, v, in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking=sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('\nRANKING DOS JOGADORES')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
print('='*35)

print('CARTEIRA DE TRABALHO')
print('-'*35)
from datetime import datetime
dados=dict()
dados['nome']=str(input('Nome: '))
nasc=int(input('Ano de Nascimento: '))
dados['idade']=datetime.now().year-nasc
dados['ctps']=int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação']=int(input('Ano de Contratação: '))
    dados['salario']=float(input('Salário: R$'))
    dados['aposentadoria']= dados['idade'] + (dados['contratação'] + 35) - datetime.now().year
print('-'*35)
for k, v in dados.items():
    print(f' - {k} tem o valor {v}')
print('='*35)

