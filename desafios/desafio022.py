print('VERFICADOR/VALIDAÇÃO DE GÊNERO')
sexo=str(input('Informe seu gênero [M/F]: ')).strip().upper()[0]
# o fatiamento [0] é pra usar apenas a primeira letra do input
while sexo not in 'MF':
    print('Dados inválidos.')
    sexo=str(input('Digite novamente: ')).strip().upper()[0]
print('Gênero {} registrado com sucesso.'.format(sexo))
print('--FIM--')
print('-'*35)

print('SORTEANDO NÚMEROS')
import random
from time import sleep
pc=random.randint(0,10)
print('Olá, vamos brincar de adivinhar!')
sleep(1)
print('Pensei em um número entre 0 e 10.')
acertou=False
palpite=0
sleep(1)
while not acertou:
    sleep(1)
    sorteio=int(input('Qual seu palpite? '))
    palpite += 1
    if sorteio == pc:
        acertou = True
    else:
        sleep(1)
        if sorteio<pc:
            print('Mais...Tente outra vez.')
        elif sorteio>pc:
            print('Menos...Tente outra vez.')
print('Acertou com {} tentativas. Parabéns!!!'.format(palpite))
