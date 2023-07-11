idade=int(input('Qual a sua idade? '))
if idade>=30:
    print('Você está ficando velho!!!')
else:
    print('Você ainda é jovem!!!!')
print('----FIM---')

nome=str(input('Qual é seu nome? '))
if nome == 'Mario':
    print('Prazer {}, você é muito inteligente!!'.format(nome))
else:
    print('Prazer {}, você é simpático.'.format(nome))
print('--FIM--')

salario=float(input('Qual é o seu salário?R$'))
print('Parabéns! Você ganha bem!' if salario>=5000.00 else 'Que ruim, você ganha mal!')
print('--FIM--\t')

n1=float(input('Digite a primeira nota: '))
n2=float(input('Digite a segunda nota: '))
m=(n1+n2)/2
if m>=7.5:
    print('Sua média é {:.1f}.\nParabéns, você foi APROVADO!'.format(m))
else:
    print('Sua média é {:.1f}.\nQue pena, você foi REPROVADO.'.format(m))
print('--FIM--')
