print('EXERCICIO VOTAÇÃO')

def voto(ano):
    from datetime import date
    atual=date.today().year
    idade = atual - ano
    if idade<16 :
         return f'Você tem {idade} anos, votação NEGADA'
    elif idade>=16 and idade<18 or idade>65 :
        return f'Você tem {idade} anos, votação OPCIONAL'
    else:
        return f'Você tem {idade} anos, votação OBRIGATORIA'
        
nasc = int(input('Qual seu ano de nascimento? '))
print(voto(nasc))

print('='*35)
print('EXERCICIO FATORIAL')

def fatorial(num, show=False):
    """_summary_
    Calcula o fatorial de um numero, com opção de exibir calculo na tela
    Args:
        num (_int_): _numero do fatorial_
        show (bool, optional): _criterio para exibir calculo na tela_. Defaults to False.

    Returns:
        _int_: _exibe o fatorial do numero com ou sem o calculo completo_
    """
    from math import factorial
    if show == True:
        c = num
        f = 1
        print(f'Calculando {num}! = ', end='')
        while c>0:
            print(f'{c}', end='')
            print(' x ' if c>1 else ' = ', end='')
            f *= c
            c -= 1   
        return f   
    else:
      f=factorial(num)  
      return f'O fatorial de {num} é {f}'   

print(fatorial(5))
#help(fatorial)

print('='*35)
print('EXERICIO FICHA JOGADOR')

def ficha(nome='desconhecido', gols=0):
    print(f'O jogador {nome} fez {gols} gols(s) no campeonato')
    
n = str(input('Nome do jogador: '))
g = str(input('Numero de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)

print('='*35)
print('EXERCICIO VALIDA NUMERO')

def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO! Digite um numero inteiro valido.')
        if ok:
            break
    return valor
        
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar: {n}')

print('='*35)
print('EXERCICIO DICIONARIO NOTAS')

def notas(*n, sit=False):
    """_summary_
    Dicionario para informar quantidade variavel de notas exibir a maior e menor com a media
    A exibição da situação é opcional
    Args:
        sit (bool, optional): criterio para exibir a situação. Defaults to False.

    Returns:
        _dict_: _retorna o dicionario com as informações definidas_
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'APROVADO'
        elif r['media'] >= 5:
            r['situação'] = 'RECUPERAÇÃO'
        else:
            r['situação'] = 'REPROVADO'
    return r

resp = notas(5, 6, 7, sit=True)
print(resp)
#help(notas)