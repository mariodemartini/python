print('SEQUENCIA FIBONACCI')
n=int(input('Quantos termos você quer ver? '))
t1=0
t2=1
print('{} - {}'.format(t1, t2), end='')
cont=3
while cont<=n:
    t3=t1+t2
    print(' - {}'.format(t3), end='') 
    t1=t2
    t2=t3
    cont+=1
print('\n--FIM--')
print('-'*35)
# na sequencia o t1 e t2 são fixos, depois pra saber o t3 é a soma
# dentro do laço determina que t1=t2 e t2=t3 os números vão pra proxima casa durante a repetição.

print('LEITURA E SOMA DE NÚMEROS')
num=0
c=0
total=0
# num = cont = total = 0 - pq todas são o mesmo numero
while num!=999:
    num=int(input('Digite um número (999 p/ parar): '))
    if num!=999:
        total+=num
        c+=1
print('O total de números digitados foi {} e a soma entre eles é {}'.format(c, total))
print('-'*35)

print('ANALISANDO NÚMEROS')
c1 = tot = media = 0
maior = menor = 0
resp='S'
while resp=='S':
    n1=int(input('Digite um número: '))
    tot+=n1
    c1+=1
# ESTAVA ERRANDO NO CONTADOR - O primeiro número é o maior e o menor, então c1 tem que ser 1 (primeiro)
    if c1==1:
        menor = maior = n1
    else:
        if n1>maior:
            maior = n1
        if n1<menor:
            menor = n1   
    resp=str(input('Quer continuar [S/N]? ')).upper()
media=tot/c1
print('\nO total digitado foi {} com média de {:.1f}'.format(tot, media))
print('O menor é {} e o maior é {}'.format(menor, maior))
print('-'*35)


    

