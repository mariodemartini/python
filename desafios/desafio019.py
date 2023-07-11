print('MAIORES DE IDADE') 
from datetime import date
atual=date.today().year
maior=0
menor=0
for c in range (1, 8):
    ano=int(input('Qual o ano a {}ª pessoa nasceu? '.format(c)))
    idade=atual-ano
    if idade>=21:
        maior += 1
    else:
        menor += 1
print('Considerando a maioridade 21 anos:')
print('Temos {} pessoas maiores de idade e {} menores de idade.'.format(maior, menor))
print('-'*35)

print('PESO DAS PESSOAS')
pmaior=0
pmenor=0
acum=0
for cont in range (1, 6):
    peso=float(input('Qual o peso(kg) da {}ª pessoa? '.format(cont)))
    acum += peso
    if peso==acum:
        pmaior=peso
        pmenor=peso
    elif peso>pmaior:
        pmaior=peso
    elif peso<pmenor:
        pmenor=peso
print('O peso menor é {}kg e o peso maior é {}kg'.format(pmenor, pmaior))

