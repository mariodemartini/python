import random
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
a5 = str(input('Quinto aluno: '))
lista = [a1, a2, a3, a4, a5]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))

print('-'*25)

n1 = str(input('Nome 1: '))
n2 = str(input('Nome 2: '))
n3 = str(input('Nome 3: '))
n4 = str(input('Nome 4: '))
n5 = str(input('Nome 5: '))
ordem = [n1, n2, n3, n4, n5]
random.shuffle(ordem)
print('A ordem de apresentação será ')
print(ordem)

print('-'*25)




