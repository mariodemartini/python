tempc = float(input('Informe a temperatura em °C: '))
tempf = 9*tempc/5+32
print('A temperatura em Fahrenheit é {}°F'.format(tempf))

print('-'*25)

dias = int(input('Quantos dias de aluguel? '))
km = float(input('Quantos Km rodados? '))
p = (dias*60)+(km*0.15)
print('O preço do aluguel é R${}'.format(p))

print('-'*25)
