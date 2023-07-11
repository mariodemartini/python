print('PROGRESSÃO ARITMÉTICA')
num=int(input('Digite o primeiro número: '))
razao=int(input('Digite a razão/constante: '))
a=num+(10-1)*razao
# formula para encontrar o décimo termo da PA.
# no range tem que colocar a + razão para incluir todos ou encontrar o valor do décimo primeiro 
for c in range(num, a+razao, razao):
    print(c, end=' ')
print('\n--FIM--')
print('-'*35)

print('NÚMEROS PRIMOS')
n=int(input('Digite um número (maior que 1): '))
t=0
for c1 in range (1, n+1):
    if n%c1==0:
        print('\033[32m', end=' ')
        t+=1
    else:
        print('\033[31m', end=' ')
    print(c1, end=' ')
print('\033[m\nO número {} foi divisivel {} vezes.'.format(n, t))
if t==2:
    print('Por isso É PRIMO!')
else:
    print('Por isso ele NÃO É PRIMO!')
print('-FIM-')
print('-'*35)
