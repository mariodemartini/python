print('LISTAS - PAR E IMPAR')
print('='*30)
lista=list()
par=[]
impar=[]
while True:
    n=int(input('Digite um número (000 p/ parar): '))
    if n==000:
        break
    else:
        lista.append(n)
        if n%2==0:
            par.append(n)
        else:
            impar.append(n)
print('-'*30)
print(f'A lista completa dos números é {lista}')
print(f'A lista com os números pares é {par}')
print(f'A lista com os números impares é {impar}')
print('='*30)

    