print('Analisando Dados')
print('='*40)
cad=list()
dado=list()
mai=men=0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(cad)==0:
        mai=men=dado[1]
    else:
        if dado[1]>mai:
            mai=dado[1]
        if dado[1]<men:
            men=dado[1]
    cad.append(dado[:])
    dado.clear()
    r=' '
    r=str(input('Quer continuar?[S/N] ')).upper()[0]
    if r=='N':
        break
print('='*40)
print(f'Foram cadastradas {len(cad)} pessoas.')
print(f'O maior peso é {mai}kg, de ',end='')
for p in cad:
    if p[1]==mai:
        print(f'{p[0]}',end=', ')
print(f'\nO menor peso é {men}kg, de ',end='')
for p in cad:
    if p[1]==men:
        print(f'{p[0]}',end=', ')

        
 
