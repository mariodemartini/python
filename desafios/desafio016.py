print('---JOKEN PO----')
import random
from time import sleep
a='PEDRA'
b='PAPEL'
c='TESOURA'
lista = [a, b, c]
comp = random.choice(lista)
pessoa=str(input('Escolha Pedra, Papel ou Tesoura: ')).upper()
sleep(1)
if comp==pessoa:
    print('O computador escolheu {} e você escolheu {}. Joguem outra vez.'.format(comp, pessoa))
elif comp=='PEDRA' and pessoa=='TESOURA':
    print('O computador escolheu {} e você escolheu {}. COMPUTADOR GANHOU!!!.'.format(comp, pessoa))
elif comp=='PAPEL' and pessoa=='PEDRA':
    print('O computador escolheu {} e você escolheu {}. COMPUTADOR GANHOU!!!.'.format(comp, pessoa))
elif comp=='TESOURA' and pessoa=='PAPEL':
    print('O computador escolheu {} e você escolheu {}. COMPUTADOR GANHOU!!!.'.format(comp, pessoa))
elif comp=='PEDRA' and pessoa=='PAPEL':
    print('O computador escolheu {} e você escolheu {}. VOCÊ GANHOU!!PARABÉNS!!!.'.format(comp, pessoa))
elif comp=='PAPEL' and pessoa=='TESOURA':
    print('O computador escolheu {} e você escolheu {}. VOCÊ GANHOU!!PARABÉNS!!!.'.format(comp, pessoa))
elif comp=='TESOURA' and pessoa=='PEDRA':
    print('O computador escolheu {} e você escolheu {}. VOCÊ GANHOU!!PARABÉNS!!!.'.format(comp, pessoa))
print('Quer jogar de novo?!!!!')
print('----'*20)

print('FINANCIAMENTO DA CASA!')
financ=float(input('Qual o valor a ser financiado? R$'))
salario=float(input('Qual o seu salário? R$'))
tempo=int(input('Em quantos meses será o financiamento? '))
prest=financ/tempo
limite=salario*0.30
if prest<=limite:
    print('O seu financiamento foi APROVADO. Seu limite é de R${:.2f} e a prestação é de R${:.2f}.'.format(limite, prest))
else:
    print('O financiamento foi RECUSADO. Seu limite é de R${:.2f} e a prestação é de R${:.2f}.'.format(limite, prest))
print('----FIM----')
