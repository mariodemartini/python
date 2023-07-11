# estrutura de repetição com VARIÁVEL DE CONTROLE
for cont in range(0, 5):
    print('OI') 
print('TCHAU!')  

for cont1 in range(0,5):
    print('Oi')
    print('Tchau!')
# a indentação determina o laço de repetição.
# a contagem termina no ultimo numero, por isso inicia em ZERO.
# se iniciar com UM a contagem vai até QUATRO, pq o quinto número para.
for cont2 in range(0, 6):
    print(cont2)
print('FIM')
# contagem regressiva precisa tirar UM (-1)
for cont3 in range(6,0,-1):
    print(cont3)
print('FIM')
# para pular números tem que indicar o valor.
for cont4 in range(0,7,2):
    print(cont4)
print('FIM')
# para determinar a contagem, inicio, fim, etec..SEMPRE colocar numero +1 para chegar onde quer.
n=int(input('Digite um número: '))
for cont5 in range (1, n+1):
    print(cont5)
print('ACABOU')

inicio=int(input('Digite o inicio: '))
fim=int(input('Digite o fim: '))
interv=int(input('Digite o intervalo: '))
for cont6 in range (inicio, fim+1, interv):
    print(cont6)
print('ACABOU')
# para repetir os inputs é só colocar dentro do for
for c in range (0, 3):
    n1=int(input('Digite um número: '))
print('NEXT')
# soma dos números digitados, inicio a variavel com zero igual no portugol.
# soma = soma + n ou soma += n
soma=0
for c1 in range (0,3):
    n2=int(input('Digite um número: '))
    soma += n2
print('A soma entre os número digitados é', soma)
