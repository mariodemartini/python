from uteis import numeros
# se não quiser importar todas as funções: 
# from uteis import fatorial

num = int(input('Digite um número: '))
print(f'O fatorial de {num} é {numeros.fatorial(num)}')
print(f'O dobro de {num} é {numeros.dobro(num)}')
print(f'O triplo de {num} é {numeros.triplo(num)}')

# PACOTES = bibliotecas:
'''
São pastas com arquivos com funções especificas
Posso ter varios modulos com diferentes funções dentro da pasta(PACOTE) e importar
* Importar o pacote inteiro - import (nome do pacote) = import uteis
* Importar o modulo especifico - from (nome do pacote) import (nome do modulo) = from uteis import data

'''