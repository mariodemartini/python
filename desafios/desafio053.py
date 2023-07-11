def linha():    
    print('-'*30)
def area(b, h):
    a = (b * h)
    print(f'A área do terreno com {b} de comprimento e {h} de largura é {a}m².')
    
print('COMPRIMENTO DE TERRENOS')   
linha()  
area(b=float(input('Comprimento (m): ')), h=float(input('Largura (m): ')))
linha()

    
