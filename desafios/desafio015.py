print('ALISTAMENTO MILITAR')
from datetime import date
atual=date.today().year
nome=str(input('Qual seu nome? '))
sexo=str(input('Qual seu gênero (M/F)? ')).upper()
ano=int(input('Qual seu ano de nascimento? '))
idade=atual-ano
if sexo=='F':
    print('Olá {}, seu alistamento militar não é obrigatório.'.format(nome))
elif sexo=='M' and idade==18:  
    print('Olá {}, você tem {} anos em {} e precisa se alistar esse ano.'.format(nome, idade, atual))
elif sexo=='M' and idade<18:
    alist=18-idade
    print('Olá {}, você tem {} anos em {} e faltam {} anos para seu alistamento.'.format(nome, idade, atual, alist))
elif sexo=='M'and idade>18:
    alist=idade-18
    print('Olá {}, você tem {} anos em {}, já passou {} anos do seu alistamento.'.format(nome, idade, atual, alist))
print('-'*35)

print('Classificação da Catergoria de Natação.')
ano1=int(input('Qual ano do seu nascimento? '))
id=atual-ano1
print('Você tem {} anos.'.format(id))
if id<=9:
    print('Você está na categoria MIRIM.')
elif id<=14:
    print('Você está na categoria INFANTIL.')
elif id<=18:
    print('Você está na categoria JUNIOR.')
elif id<=25:
    print('Você está na categoria SENIOR.')
else:
    print('Você está na categoria MASTER.')
print('---FIM--')

print('CALCULANDO IMC')
altura=float(input('Qual a sua altura(metros)? '))
peso=float(input('Qual o seu peso(kg)? '))
imc=peso/(altura**2)
if imc < 18.5:
    print('Seu IMC é {:.1f} - ABAIXO DO PESO'.format(imc))
elif imc>=18.5 and imc<25:
    print('Seu IMC é {:.1f} - PESO IDEAL'.format(imc))
elif imc>=25 and imc<30:
    print('Seu IMC é {:.1f} - SOBREPESO'.format(imc))
elif imc>=30 and imc<=40:
    print('Seu IMC é {:.1f} - OBESIDADE'.format(imc))
elif imc>40:
    print('Seu IMC é {:.1f} - OBESIDADE MÓRBIDA'.format(imc))
print('---FIM---')
