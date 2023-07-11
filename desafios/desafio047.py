print('BOLETIM ESCOLAR')
print('='*30)
boletim=list()
while True:
    nome=str(input('Digite o nome do aluno: '))
    n1=float(input('Digite a nota 1: '))
    n2=float(input('Digite a nota 2: '))
    media=(n1+n2)/2
    boletim.append([nome,[n1, n2],media])
    resp=' '
    while resp not in 'SN':
        resp=str(input(
            'Quer cadastrar mais alunos? [S/N] ')).upper()
    if resp=='N':
        break
print('-'*25)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*25)
for i, a in enumerate(boletim):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*25)
    opc=int(input('Mostrar notas de qual aluno?(999 para) '))
    if opc==999:
        print('FINALIZANDO....')
        break
    if opc<=len(boletim)-1:
        print(f'Notas de {boletim[opc][0]} são {boletim[opc][1]}')
        print('VOLTE SEMPRE!')
        
    


    
    