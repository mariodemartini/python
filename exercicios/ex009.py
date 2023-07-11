# Estrutura de repetição com COM TESTE LÓGICO
# quando não sei o limite, e não tem padrão
# ENQUANTO não acontece oq quero (condição)
#    faça isso
# PARE
# 
# WHILE NOT condição:
#   faça alguma coisa
# ACABA
c=1 
while c<10:
    print(c)
    c+=1
print('FIM')
# exemplo de looping finito com flag
r='S'
while r=='S':
    n1=float(input('Digite um valor: '))
    r=str(input('Quer continuar?[S/N] ')).upper()
print('FIM')
# Outro Exemplo
a=1
par = impar = 0 
while a!=0:
    a=int(input('Digite um número (0 p/ parar):'))
    if a != 0:
        if a%2==0:
            par+=1
        else:
            impar += 1
print('Você digitou {} números pares e {} números impares.'.format(par, impar))

# exemplo de looping infinito
# n=1
# while n!=0:
#     n=int(input('Digite um numero: '))
# print('FIM')


