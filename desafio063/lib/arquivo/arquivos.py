from lib.interface.menus import cabecalho

def arquivo_existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
    
def criar_arquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve erro na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso')
        
        
def ler_arquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabecalho('LISTAR PESSOAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '') 
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade='0'):
    try:
        a = open(arq, 'at')
    except:
        print('Erro na abertura do arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve erro ao gravar os dados')
        else:
            print('Novo registro adicionado')
            a.close()
        