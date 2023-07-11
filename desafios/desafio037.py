print('LENDO VALORES DA LISTA')
print('='*40)
valores=[]
for cont in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))
print('-'*40)
print(f'O valores digitados foram {valores}')
print(f'O maior valor foi {max(valores)} na(s) posição(ões): ',end='')
for p, v in enumerate(valores):
    if v==max(valores):
        print(f'{p}...',end='')
print(f'\nO menor valor foi {min(valores)} na(s) posição(ões): ',end='')
for p, v in enumerate(valores):
    if v==min(valores):
        print(f'{p}...',end='')
print('\nFIM')
print('='*40)

    

    