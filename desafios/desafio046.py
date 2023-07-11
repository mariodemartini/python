print('='*30)
print('PALPITES MEGA SENA')
print('='*30)
from random import randint
from time import sleep
jogo=[]
total=[]
palpite=int(input('Informe quantos jogos: '))
print('-'*30)
cont=0
while cont<=palpite:
    numero=0
    while True:
        n=randint(1,60)
        if n not in jogo:
            jogo.append(n)
            numero+=1
        if numero>=6:
            break
    cont+=1
    jogo.sort()
    total.append(jogo[:])
    jogo.clear()
for p in range(0,len(total)):
    sleep(1)
    print(f'Jogo {p+1}: {total[p]}')
print('='*30)


        

    