print('FICHA DE TREINAMENTO')
print('='*30)
from audioop import reverse
from random import randint
from random import choice     
nome=str(input('Nome: '))
sem=int(input('Semanas de Treino: '))
objt=int(input('''Objetivos:
[1] Adaptação
[2] Emagrecimento
[3] Hipertrofia
[4] Força
Qual sua escolha? '''))
print('-'*30)
ficha=list()
total=list()
metodo=('CIRCUITO', 'BI SET', 'TRI SET', 'PIRÂMIDE CRESCENTE', 'PIRÂMIDE DESCRESCENTE', 'SUPER SET', 'DROP SET')
cont=1
if objt==1:
    while cont<=sem:
        s=randint(2,4)
        r=randint(10,15)
        cont+=1
        ficha.append([s,r])
        total.append(ficha[:])
        ficha.clear()
    total.sort()
    for p in range(0,len(total)):
        print(f'Semana {p+1:^2} - {total[p][0][0]:^2} X {total[p][0][1]:^4}')
if objt==2:
    while cont<=sem:
        s=randint(3,4)
        if s==3:
            r=randint(12,20)
        if s==4:
            r=randint(10,15)
        escolha=choice(metodo)
        cont+=1
        ficha.append([s,r, escolha])
        total.append(ficha[:])
        ficha.clear()
    total.sort()
    for p in range(0,len(total)):
        print(f'Semana {p+1:^2} - {total[p][0][0]:^2} X {total[p][0][1]:^4} - {total[p][0][2]}')
if objt==3:
    while cont<=sem:
        s=randint(3,5)
        r=randint(8,15)
        escolha=choice(metodo)
        cont+=1
        ficha.append([s,r, escolha])
        total.append(ficha[:])
        ficha.clear()
    total.sort()
    for p in range(0,len(total)):
        print(f'Semana {p+1:^2} - {total[p][0][0]:^2} X {total[p][0][1]:^4} - {total[p][0][2]}')
if objt==4:
    while cont<=sem:
        s=randint(4,7)
        r=randint(1,6)
        cont+=1
        ficha.append([s,r])
        total.append(ficha[:])
        ficha.clear()
    total.sort()
    for p in range(0,len(total)):
        print(f'Semana {p+1:^2} - {total[p][0][0]:^2} X {total[p][0][1]:^4}')
print('='*30)


    

