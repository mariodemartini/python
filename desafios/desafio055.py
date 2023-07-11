from time import sleep
def contador(inicio, fim, passo):
    print('-'*35)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
    if passo<0:
        passo *= -1
    if passo==0:
        passo=1
    if inicio<fim:
        for c in range(inicio, fim+1, passo):
            print(c, end=' ')
            sleep(0.5)
        print('FIM')
    else:
        cont=inicio
        while cont>=fim:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont -= passo 
        print('FIM')
    print('-'*35)
    
contador(1, 10, 1)
contador(10, 1, 2)
print('AGORA É SUA VEZ:')
contador(inicio=int(input('Início: ')), fim=int(input('Fim: ')), passo=int(input('Passo: ')))