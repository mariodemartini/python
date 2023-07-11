from lib.interface.menus import *
from lib.arquivo.arquivos import *

arq = 'desafio063/cursoemvideo.txt'
if not arquivo_existe(arq):
    criar_arquivo(arq)
    
while True:
    resp = menu(['Cadastrar Pessoas', 'Listar Pessoas', 'Sair'])
    if resp == 1:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leia_int('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 2:
        ler_arquivo(arq)
    elif resp == 3:
        cabecalho('Saindo do Sistema')
        break
    else:
        cabecalho('ERRO! Digite novamente')
        
