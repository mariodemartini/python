print('FORMA DE PAGAMENTO')
valor=float(input('Quanto custa o produto? R$'))
forma=int(input('''Formas de PAGAMENTO: 
    [1] à vista DINHEIRO
    [2] à vista CRÉDITO OU DÉBITO
    [3] 2X no CRÉDITO
    [4] 3X ou mais no CRÉDITO
Qual é sua forma de pagamento: '''))
if forma==1:
    desc=valor-(valor*0.10)
    print('O preço com desconto é R${}'.format(desc))
elif forma==2:
    desc=valor-(valor*0.05)
    print('O preço com desconto é R${}'.format(desc))
elif forma==3:
    parcela=valor/2
    print('O preço é R${} e não tem desconto\nSua parcela é de R${}.'.format(valor, parcela))
elif forma==4:
    juros=valor+(valor*0.20)
    totp=int(input('Quantas parcelas? '))
    parcela=juros/totp
    print('O valor parcelado tem juros\nO preço é R${} com parcelas de R${}'.format(juros, parcela)) 
else:
    print('\033[31mOPÇÃO INVÁLIDA\033[m')
print('---FIM---')

print('COMPARANDO NÚMEROS')
a=int(input('Digite um número: '))
b=int(input('Digite outro número: '))
if a>b:
    print('O primeiro número é maior.')
elif b>a:
    print('O segundo número é maior.')
else:
    print('Os dois números são iguais.')
print('-'*35)

print('MÉDIA DA ESCOLA')
n1=float(input('Digite a primeira nota: '))
n2=float(input('Digite a segunda nota: '))
n3=float(input('Digite a terceira nota: '))
media=(n1+n2+n3)/3
if media<5: 
    print('Você teve média {:.2f}. Está REPROVADO!'.format(media))
elif media>=5 and media<=7.4:
    print('Você teve média {:.2f}. Está de RECUPERAÇÃO!'.format(media))
elif media>=7.5:
    print('Você teve média {:.2f}. Está APROVADO!'.format(media))
print('--FIM--')