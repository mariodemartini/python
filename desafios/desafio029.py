print('='*50)
print('JOGO PAR OU IMPAR')
print('-'*35)
from random import randint
from time import sleep
vit=0
while True:
    escolha=' '
    while escolha not in 'PI':
        escolha=str(input('Escolha Par ou Impar [P/I]: ')).upper().strip()[0]
    jogador=int(input('Jogue um número: '))
    sleep(2)
    pc=randint(0,10)
    resultado=(pc+jogador)
    if resultado%2==0 and escolha=='P':
        print(f'O computador jogou {pc} e você jogou {jogador}. Deu PAR.')
        sleep(1)
        print('\nParabéns! Você VENCEU!!!!')
        print('-'*35)
    if resultado%2>0 and escolha=='I':
        print(f'O computador jogou {pc} e você jogou {jogador}. Deu IMPAR.')
        sleep(1)
        print('\nParabéns! Você VENCEU!!!!')
        print('-'*35)
    if resultado%2==0 and escolha=='I':
        print(f'O computador jogou {pc} e você jogou {jogador}. Deu PAR.')
        sleep(1)
        print('\nVocê Perdeu! GAME OVER!!!')
        print('-'*35)
        break
    if resultado%2>0 and escolha=='P':
        print(f'O computador jogou {pc} e você jogou {jogador}. Deu IMPAR.')
        sleep(1)
        print('\nVocê Perdeu! GAME OVER!!!')
        print('-'*35)
        break
    print('Vamos jogar novamente...')
    vit+=1
print(f'Você venceu {vit} disputas consecutivas.')
print('='*50)
    


