# while True:
#     if sim:
#         passo
#     if vazio:
#         pula
#     if tem:
#         pega
#     if trofeu:
#         pula
#         break - comando para terminar o looping/repretição.
# pega/ganha.

# cont=1
# # substituir cont<=10 por True (infinito dentro da condição)
# while True: 
#     print(cont,'->',end='')
#     cont+=1
# print('Acabou')

n = s = 0
while True:
  n=int(input('Digite um número:'))
  if n==999:
      break 
  s += n
# print('Acabou')
print(f'A soma dos números é {s}')
# fstring (f de format) - f antes das aspas posso colocar a variavel dentro do {}
nome='José'
idade=53
print(f'O {nome} tem {idade} anos.')
