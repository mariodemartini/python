def aumentar(preco=0, taxa=0):
    res = preco + (preco * taxa/100)
    return res


def diminuir(preco=0, taxa=0):
    res = preco - (preco * taxa/100)
    return res


def metade(preco=0):
    res = preco / 2
    return res


def dobro(preco=0):
    res = preco * 2
    return res


def resumo(p, t):
    print(f'O preço com aumento de {t}% é: R${aumentar(p, t):.2f}')
    print(f'O preço com desconto de {t}% é: R${diminuir(p, t):.2f}')
    print(f'A metade do preço é: R${metade(p):.2f}')
    print(f'O dobro do preço é: R${dobro(p):.2f}')

    
def leia_dinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print('ERRO! Preço inválido!')
        else:
            valido = True
            return float(entrada)
        
        
def leia_taxa(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.')
        if entrada.isalpha() or entrada.strip() == '':
            print('ERRO! Taxa inválida!')
        else:
            valido = True
            return float(entrada)
