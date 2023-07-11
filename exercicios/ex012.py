print('Variáveis Compostas - LISTAS')
# listas usa [ ] e são mutáveis.
# lista.append('objeto') - acrescenta um item no final da lista.
# lista.insert(n local, 'objeto') - acrescenta item na posição n que eu quiser e os outros itens "andam" pra frente.

# del lista[posição] - exclui o item da posição/indice
# lista.pop(posição) - elimina o item do indice determinado
# lista.pop() - qdo vazio elimina o ultimo item
# lista.remove('objeto') - exclui o objeto determinado, sempre o primeiro encontrado.
# A lista é reorganizada automáticamente qdo excluimos um item.
# Caso eu deletar um item que não tem o programa dá erro
# if 'objeto' in lista:
#       lista.remove('objeto') - só remove se o item existir

# valores= list (range(4,11)) - cria uma lista com os itens determinados de 4 a 10 com nome valores e o indice de 0 a 6 para o valor respectivo.

# valores aleatórios - posso declarar do jeito que eu quiser, sem ordem.
# valores.sort() organiza na ordem do menor pro maior.
# valores.sort(reverse=True) - organiza ao contrário.
# len(valores) mostra o tamanho da lista.

num = [2,5,9,1]
num[2] = 3
# trocou o 9 pelo 3
print(num)

num1 = [2,5,9,1]
num1.append(7)
# acrescenta o 7
num1.sort()
print(num1)

n=[2,5,9,1,7]
n.sort(reverse=True)
n.insert(2, 0)
# acrescentou o 0 na terceira posição(contando o inicio em 0)
# não aplicou a organização pq o comando está depois.
print(n)
print(f'Essa lista tem {len(n)} elementos')

n1=[2,5,9,1,7,9]
n1.pop()
# pop - para remover coloco o indice 
n1.remove(9)
# remove - para remover coloco o elemento
print(n1)

valores=[]
# valores=list()
valores.append(5)
valores.append(9)
valores.append(4)
for v in valores:
    print(f'{v}...')
    
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('Cheguei ao final da lista')
    
numeros=[]
for cont in range(0,5):
    numeros.append(int(input('Digite um valor: ')))
print(numeros)

a=[2,3,4,7]
b=a[:]
# esse método cria uma cópia com as listas independentes, senão as duas executam as mesmas coisa, uma interfere na outra.
b[2]=8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
