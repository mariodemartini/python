print('NÚMEROS ALEATÓRIOS')
print('='*50)

from random import randint
num=(randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print('Os valores sorteados foram:')
for n in num:
    print(f'{n}',end=' ')
print(f'\nO maior valor sorteado foi: {max(num)}')
print(f'O menor valor sorteado foi: {min(num)}')
print('='*50)

    