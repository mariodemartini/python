print('='*35)
print('TABUADA')
print('-'*35)
while True:
    n=int(input('Quer ver a tabuada de qual número (-1 p/ PARAR)? '))
    print('-'*35)
    if n<0:
        break
    for multi in range(1,11):
        res = n * multi
        print(f'{n} X {multi:2} = {res:2}')
    print('-'*35)
print('Programa Encerrado.')
print('OBRIGADO, Volte Sempre!')
print('='*50)