print('Variáveis Compostas - TUPLAS')
# armazenar mais um "item" dentro da variável.
# AS TUPLAS SÃO IMUTÁVEIS - depois de registrados não dá pra mudar enquanto está executando, precisa alterar a declaração.
# Usamos o fatiamento para selecionar os itens da tupla.
# fatiamento inicia em 0 e não exibe o ultimo - No exemplo temos 0 1 2 3 (4 elementos)
# podemos ter dados de tipos diferentes dentro da tupla - str, float, int
# del apaga a tupla inteira
lanche=('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[:3])
print(len(lanche))
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba')

for cont in range(0, len(lanche)):
    print(lanche[cont])
# lanche cont só mostra as posições - [cont] mostra os nomes

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
    
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} e na posição {pos}')
# pos = posição da lista, e o enumerate mostra os elementos na posição.

print(sorted(lanche))
# sorted - ordem alfabética

a=(2, 5, 4)
b=(5, 8, 1, 2)
c= b + a 
print(c.index(5, 1))
# NÃO VAI SOMAR AS TUPLAS, VAI MOSTRAR AS DUAS NA ORDEM DETERMINADA - B DEPOIS A
# c.count mostra quantas vezes aparece o item na tupla.
# c.index mostra a posição do elemento da primeira ocorrencia
# c.index(5, 1) mostra o número 5 a partir da posição 1


