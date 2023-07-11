print('CADASTRO DE PESSOAS')
print('='*50)
cadastro = pessoa18 = mulher20 = homem = 0
while True:
    idade=int(input('Informe IDADE: '))
    sexo=' '
    while sexo not in 'MF':
        sexo=str(input('Informe SEXO [M/F]: ')).strip().upper()[0]
    print('-'*30)
    if idade>18:
        pessoa18+=1
    if idade<20 and sexo=='F':
        mulher20+=1
    if sexo=='M':
        homem+=1
    cadastro+=1
    resp=' '
    while resp not in 'SN':
        resp=str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    print('='*30)
    if resp=='N':
        break  
print(f'Foram cadastradas {cadastro} pessoas.')
print(f'Foram cadastradas {pessoa18} pessoas acima de 18 anos.')
print(f'Foram cadastradas {mulher20} mulheres abaixo de 20 anos.')
print(f'Foram cadastrados {homem} homens.')
print('='*50)

