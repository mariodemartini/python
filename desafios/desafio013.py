print('ANALISANDO TRIÂNGULOS')
a=float(input('Digite o primeiro comprimento de reta: '))
b=float(input('Digite o segundo comprimento de reta: '))
c=float(input('Digite o terceiro comprimento de reta: '))
if a<b+c and b<a+c and c<a+b:
    print('Podemos formar um triângulo')
    if a!=b!=c!=a:
        print('\033[32mESCALENO\033[m.')
    elif a==b==c:
        print('\033[33mEQUILÁTEO\033[m.')
    else:
        print('\033[34mISÓCELES\033[m.')
else:
    print('\033[31mNão é possível\033[m formar um triângulo.')
print('---FIM---')    


print('CONVERSOR DE BASES')
num=int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:'
      [1] converter para BINÁRIO
      [2] converter para OCTAL
      [3] converter para HEXADECIMAL''')
opcao=int(input('Sua opção: '))
if opcao==1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opcao==2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opcao==3:
    print('{} convertido para HEXEDECIMAL é igual a {}'.format(num, hex(num[2:])))
else:
    print('OPÇÃO INVÁLIDA.')
    
    