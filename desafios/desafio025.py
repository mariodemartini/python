print('PROGRESSÃO ARITMÉTICA 2')
n=int(input('Informe o primeiro termo: '))
r=int(input('Informe a razão: '))
a=n+(10-1)*r
c=n
print('A PA é:', n, end=' ')
while c<a:
    c+=r
    print(c, end=' ')
print('\n--FIM--')
print('-'*35)

print('PROGRESSÃO ARITMÉTICA 3')
num=int(input('Informe o primeiro termo: '))
razao=int(input('Informa razão/constante: '))
termo=num
cont=1
total=0
mais=10
while mais!=0:
    total += mais
    while cont<=total:
        print('{} - '.format(termo), end='')
        termo+=razao
        cont+=1
    print('PAUSA')
    mais=int(input('Quantos termos você quer a mais? '))
print('\nPA finalizada com {} termos mostrados.'.format(total))
print('-'*35)
# A variavel o total é pra saber o ultimo termo da PA 
# A variavel mais é a condição de parada com valor 10 pq é o minimo que quero ver no inicio.
