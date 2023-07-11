print('VALIDANDO EXPRESSÕES MATEMÁTICAS')
print('='*40)
expr=str(input('Digite a expressão: '))
pilha=[]
for simb in expr:
    if simb=='(':
        pilha.append('(')
    elif simb==')':
        if len(pilha)>0:
            pilha.pop()
            # o primeiro if adiciona o parenteses, agora remove o parenteses pra ver se sobra algum.
        else:
            pilha.append(')')
            break
if len(pilha)==0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')

