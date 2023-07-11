print('ANALISANDO NÚMEROS')
print('='*30)
num=list()
cont=0
while True:
    num.append(int(input('Digite um número: ')))
    cont+=1
    r=' '
    while r not in 'SN':
        r=str(input('Quer continuar?[S/N] ')).upper()
    if r=='N':
        break
num.sort(reverse=True)
print('-'*30)
print(f'Os número digitados, em ordem decrescente, foram {num}')
print(f'Foram digitados o total de {cont} números.')
# no lugar do contador podemos usar o len(num) para saber a posição do ultimo elemento.
if 5 in num:
    print(f'O número 5 foi digitado {num.count(5)} vezes.')
else:
    print('O número 5 não está na lista.')
print('='*30)
