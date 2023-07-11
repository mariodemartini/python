n1=int(input('Digite o 1º número: '))
n2=int(input('Digite o 2º número: '))
n3=int(input('Digite o 3º número: '))
# Maneira simplificada do Guanabara:
# menor = n1
# if n2<n1 and n2<n3:
#     menor = n2
# if n3<n1 and n3<n2:
#     menor = n3
# maior = n1
# if n2>n1 and n2>n3:
#     maior=n2
# if n3>n1 and n3>n2:
#     maior=n3
# print('O menor número digitado foi {}'.format(menor))
# print('O maior número digitado foi {}'.format(maior))
if n1>n2 and n2>n3:
    print('O 1º é o maior e o 3º é o menor.')
if n1>n3 and n3>n2:
    print('1º é o maior e o 2º é o menor.')
if n2>n1 and n1>n3:
    print('2º é o maior e o 3º é o menor.')
if n2>n3 and n3>n1:
    print('2º é o maior e o 1º é o menor.')
if n3>n2 and n2>n1:
     print('3º é o maior e o 1º é o menor.') 
if n3>n1 and n1>n2:
    print('3º é o maior e o 2º é o menor.') 
if n1==n2 and n1==n3:
    print('Os três números são iguais!')
print('--FIM--')

sal=float(input('Qual o seu salário? R$'))
if sal<=1250.00:
    sal1 = sal + (sal*0.15)
    print('O salário com aumento de 15% é R${}'.format(sal1))
else:
    sal1 = sal+(sal*0.10)
    print('O novo salário com aumento de 10% é R${}'.format(sal1))
# simplificado: sal1= sal+(sal*0.15) if sal<=1250.00 else sal+(sal*0.10)
print('--FIM--')
