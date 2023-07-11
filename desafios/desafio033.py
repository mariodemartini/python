print('='*35)
print('ESCREVENDO NÚMEROS POR EXTENSO')
print('-'*30)
extenso=('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n=int(input('Digite um número entre 0 e 20: '))
    if n>=0 and n<=20:
        break
    else:
        print('Tente novamente.')
print(f'O número {n} escrito por extenso é {extenso[n]}.')
print('='*50)

print('\nTABELA BRASILEIRÃO 2021')
print('-'*50)
classific=('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Red Bull Bragantino', 'Fluminense', 'América-MG', 'Atlético-GO', 'Santos', 'Ceará', 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')
print(f'Os cinco primeiros colocados foram: \n{classific[0:5]} ')
print('-'*50)

print(f'Os quatro últimos colocados foram: \n{classific[16:20]}')
print('-'*50)

print('Os times em ordem alfabética:\n',sorted(classific))
print('-'*50)

print(f'A classificação final dos times foi: \n{classific}')
print('-'*50)

print(f'A Chapecoense terminou na {classific.index("Chapecoense")+1}ª posição.')
print('='*50)