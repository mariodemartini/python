p=float(input('Qual o preço do produto? R$'))
pf=p-(p*0.05)
print('O preço com desconto é R${:.2f}'.format(pf))

print('-'*20)

sal=float(input('Qual é o seu salário? R$'))
saln=sal+(sal*15/100)
print('O seu salário com aumento é de R${:.2f}'.format(saln))

print('-'*20)
