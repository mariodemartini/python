print('ORDENANDO NÚMEROS')
print('='*30)
lista=[]
for c in range(0,5):
    n=int(input('Digite um número: '))
    if c==0:
        lista.append(n)
    elif n>lista[len(lista)-1]:
        lista.append(n)
    else:
        pos=0
        while pos<len(lista):
            if n <= lista(pos):
                lista.insert(pos, n)
                break
            pos+=1
print('-'*30)
print(f'Os valores digitados em ordem foram {lista}')
            
   
    