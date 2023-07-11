cidade = str(input('Em qual cidade você nasceu? ')).strip()
print('O nome da cidade começa com Santo? {}'.format(cidade[:5].upper()=='SANTO'))

print('-'*25)

nome = str(input('Qual é seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))

print('-'*25)

frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}.'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}.'.format(frase.rfind('A')+1))

print('-'*25)

nomecomp = str(input('Digite seu nome completo: ')).strip()
n = nomecomp.split()
print('Primeiro nome: {}'.format(n[0]))
print('Ultimo nome: {}'.format(n[len(n)-1]))

print('-'*25)








