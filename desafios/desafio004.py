din = float(input('Quanto dinheiro você tem? R$'))
dolar=din/3.27
print('A quantidade do valor em dolar é US${:.2f}'.format(dolar))
print('-'*15)
h = float(input('Qual a altura da parede em metros? '))
l = float(input('Qual a largura da parede em metros? '))
a = l*h
tinta=a/2
print('A aera total da parede é {:.2f}m² e precisa de {:.2f}l de tinta.'.format(a, tinta))

