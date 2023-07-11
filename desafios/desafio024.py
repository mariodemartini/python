from math import factorial
print('FATORIAL')
# METODO SIMPLES MOSTRANDO SÓ RESULTADO
# from math import factorial
# n=int(input('Digite um número para calcular seu fatorial:'))
# f=factorial(n)
# print('O fatorial de {} é {}'.format(n, f))
n=int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c>0:
    print('{}'.format(c), end='')
    print(' x ' if c>1 else ' = ', end='')
    f *= c
    c -= 1
    # para fazer regressivo (onde eu estava errando)
print(f)
print('-'*35)

num=int(input('Digite um número: '))
fat = num
fatorial = 1
print('Calculando {}! = '.format(num), end='')
for fat in range (fat, 0, -1):
    print(fat, end='')
    print(' x ' if fat>1 else ' = ', end='')
    fatorial *= fat
print(fatorial)
print('-'*35)
   