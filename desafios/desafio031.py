print('CADASTRO DE COMPRAS')
print('='*50)
totcomp = prodmil = barato = totgasto = 0
nbarato=' '
while True:
    nomeprod=str(input('Digite o nome do produto: ')).upper().lstrip().rstrip()
    preco=float(input('Digite o preço: R$'))
    print('-'*35)
    totcomp+=1
    totgasto+=preco
    if totcomp==1 or preco<barato:
        barato=preco
        nbarato=nomeprod
    if preco>1000:
        prodmil+=1
    resp=' '
    while resp not in 'SN':
        resp=str(input('Quer cadastrar mais produtos [S/N]? ')).upper().strip()[0]
    print('-'*35)
    if resp=='N':
        break
print(f'O total da compra de {totcomp} produtos foi de R${totgasto:.2f}')
print(f'Teve {prodmil} produtos acima de R$1000,00')
print(f'O produto mais barato foi {nbarato}, custando R${barato}.')
print(''*35)
print('OBRIGADO!!! VOLTE SEMPRE!!')
print('='*50)


