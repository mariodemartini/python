print('ANALISANDO IDADES')
somaidade=0
velho=0
nomevelho=''
# ter a variavel str aberta para conseguir guardar o nome.
menor=0
for cont in range (1, 5):
    print('--- {}ª PESSOA ---'.format(cont))
    nome=str(input('Qual seu nome? ')).strip()
    idade=int(input('Qual sua idade? '))
    sexo=str(input('Qual seu gênero?[M/F] ')).upper()
    somaidade += idade
    if sexo=='M':
        if idade>velho:
            velho=idade
            nomevelho=nome
    if sexo=='F':
        if idade<20:
            menor += 1
media=somaidade/4
print('-'*20)
print('A média de idade é {} anos\nO mais velho é {} com {} anos'.format(media, nomevelho, velho))
print('Tem {} mulher(s) com menos de 20 anos.'.format(menor))
print('---- FIM ----')