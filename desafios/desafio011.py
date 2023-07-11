from datetime import datetime
import random
from time import sleep
n=random.randint(1,5)
sorteio=int(input('Tente adivinhar o número sorteado: '))
print('PROCESSANDO...')
sleep(3)
if sorteio==n:
    print('O número sorteado foi {} e você tentou {}\nPARABÉNS!!! VOCÊ ACERTOU!!!!!'.format(n, sorteio))
else:
    print('ERROUUUUUU!!!!!!!!\nO número sorteado foi {} e você tentou {}'.format(n, sorteio))
print('JOGUE OUTRA VEZ\n--FIM--')

vel=int(input('Você passou pelo radar em qual velocidade (km/h)? '))
if vel>80:
    multa=(vel-80)*7
    print('Você foi multado em R${} por estar acima do limite de 80km/h.'.format(multa))
else:
    print('Parabéns! Você está dentro do limite de 80km/h!')
print('---FIM---')

num=int(input('Digite um número diferente de zero: '))
a=num%2
if a==0:
    print('O número é PAR!')
else:
    print('O número é IMPAR!')
print('--FIM--')

dist=int(input('Qual a distância da viagem (km): '))
if dist<=200:
    p=(dist*0.5)
    print('O preço da passagem é R${}, por percorrer {}km.'.format(p, dist))
else:
    p1=(dist*0.45)
    print('O preço da passagem é R${}, por percorrer {}km.'.format(p1, dist))
# maneira simpificada - p= dist * 0,5 if dist<=200 else dist*0,45
print('---FIM---')

from datetime import date
ano=int(input('Digite um ano qualquer (para o ano atual digite 0): '))
if ano==0:
    ano=date.today().year
if ano%4==0 and ano%100!=0 or ano%400==0:
    print('O ano', ano, 'é bissexto.')
else:
    print('O ano', ano, 'não é bissexto.')
print('--FIM--')

