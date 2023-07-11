# docstring é a documentação/manual das funções.
# posso criar a explicação da função criada por mim quando uso o def.

def contador (i, f, p):
    """_summary_
    Faz uma contagem e mostra na tela.
    Função exemplo para aprender docstring.
    Args:
        i (_int_): _inicio da contagem_
        f (_int_): _final da contagem_
        p (_int_): _passo da contagem, intervalo_
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('FIM!')
    
contador(2, 10, 2)

# parametros opcionais são valores "vazios" quando não tem na função. Exemplo: 
# def somar(a, b, c) - preciso de 3 paramentros
# def somar(a, b, c=0) - c é opcional, caso não informado vale zero. Posso colocar todos como opcionais.
#-------------------------------------------------------------------------------------------------------

def teste(b):
    #declarar variavel global dentro do local
    global a
    
    #variavel local
    b+=4
    c=2

#PROGRAMA PRINCIPAL
#variavel global
a=5
#-----------------------------------

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

print(f'A soma é: {somar(3, 5, 2)}')
#ou
resp = somar(3, 5, 2)
print(resp)
