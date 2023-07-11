print('CADASTRANDO PARES E ÍMPARES')
print('='*40)
num=[[],[]]
for c in range(1,8):
    n=int(input(f'Digite o {c}º número: '))
    if n%2==0:
        num[0].append(n)
    else:
        num[1].append(n)
print('-'*30)
num[0].sort()
num[1].sort()
print(f'Os valores pares são: {num[0]}')
print(f'Os valores impares são: {num[1]}')
print('='*30)