print('CONTAGEM REGRESSIVA')
from time import sleep
print('Iniciando contagem...')
sleep(1)
for c in range (10, 0, -1):
    print(c)
    sleep(1)
print('BUMMMMM\U0001f386\U0001f386\U0001f386\U0001f386\U0001f386BUMMMM')
print('-'*35)

print('CONTAGEM PARES')
for c1 in range (2, 51, 2):
    print(c1, end=' ')
print('\n--FIM--')
print('-'*35)
# o end='' deixa tudo na mesma linha.

print('SOMA DOS IMPARES')
s=0
cont=0
for c2 in range(1, 501, 2):
    if c2%3==0:
        cont += 1
        s += c2
print('A soma dos {} números impares e multiplos de 3 é: {}'.format(cont, s))
print('--FIM--')
print('-'*30)

print('TABUADA')
n=int(input('Digite um número para ver a tabuada: '))
for c3 in range (1, 11):
    r=c3*n
    print('{} x {:2} = {}'. format(n, c3, r))
print('--FIM--')
print('-'*35)

print('SOMA NÚMEROS PARES')
somap=0
for c4 in range (1, 7):
    n1=int(input('Digite um número: '))
    if n1%2==0:
        somap += n1
print('A soma apenas dos números pares é {}'.format(somap))
print('--FIM--') 
