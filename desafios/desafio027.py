print('LENDO NÚMEROS')
print('-'*35)
cont = soma = 0
while True:
    n=int(input('Digite um número (999 p/ PARAR): '))
    if n==999:
        break
    cont+=1
    soma+=n
print(f'\nForam digitados {cont} números e a soma total foi {soma}.')
print('\n-- FIM -- Obrigado!!')
print('='*50)

    