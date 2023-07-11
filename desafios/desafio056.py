from time import sleep
def maior(* num):
    cont = maior = 0
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor}', end=' ')
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor>maior:
                maior = valor
        cont+=1
    print(f'\nForam informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')
    print('='*30)
    
maior(2, 3, 5, 8, 9, 25)
maior(2, 8, 7, 6, 1)
maior(5)
maior()
maior(1, 100, 0)

    