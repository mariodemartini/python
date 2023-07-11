numeros = list()
while True:
    n=int(input('Digite um número: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado. Não vou adicionar...')
    r=' '
    while r not in 'SN':
        r=str(input('Quer continuar [S/N]? ')).upper()
    if r=='N':
        break
numeros.sort()
print('-'*30)
print('Os valores adicionados foram',numeros)
