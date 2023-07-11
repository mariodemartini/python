print('MENU')
from time import sleep
n1=int(input('Digite o 1º valor: '))
n2=int(input('Digite o 2º valor: '))
opcao=0
# SEMPRE INICIAR A VARIAVEL DE CONDIÇÃO ANTES
while opcao!=5:
    print('')
    print('''Escolha uma das opções: 
      [1] Somar
      [2] Multiplicar
      [3] Maior
      [4] Digitar novos números
      [5] Sair do programa''')
    opcao=int(input('Digite sua opção: '))
    print('')
    sleep(2)
    if opcao==1:
        soma=n1+n2
        print('A soma dos valores {} e {} é igual a {}'.format(n1, n2, soma))
        sleep(2)
    elif opcao==2:
        multi=n1*n2
        print('A multiplicação de {} com {} é igual a {}'.format(n1, n2, multi))
        sleep(2)
    elif opcao==3:
        if n1>n2:
            print('O 1º valor ({}) é maior que o 2º valor ({}).'.format(n1, n2))
            sleep(2)
        elif n1<n2:
            print('O 2º valor ({}) é maior que o 1º valor ({}).'.format(n2, n1))
            sleep(2)
        else:
            print('Os valores são iguais.')
            sleep(2)
    elif opcao==4:
        n1=int(input('Digite o 1º valor: '))
        n2=int(input('Digite o 2º valor: '))
    elif opcao==5:
        sair=True
        print('Encerrando..')
        sleep(3)
    else:
        print('Opção INVÁLIDA. Tente novamente.')
        sleep(2)
print('Acabou!')
print('-'*35)
         
