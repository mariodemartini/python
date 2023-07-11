print('PALÍNDROMO - MANEIRA 1')
frase=str(input('Digite uma frase: ')).strip().upper()
palavras=frase.split()
junto=''.join(palavras)
inverso=''
# for serve para fazer a leitura de tras pra frente usando len(junto)-1 para saber qual é ultima, -1 para ir até a primeira(sempre diferença de 1 por causa da regra)
# o ultimo -1 é para fazer o caminho de tras pra frente
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
    # o junto[letra] é para exibir apenas as letras da frase e não mais que isso.
print('O inverso da frase é {}.'.format(inverso))
if inverso==junto:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase NÃO é um palíndromo!')
print('------')

print('PALÍNDROMO - MANEIRA 2')
frase=str(input('Digite uma frase: ')).strip().upper()
palavras=frase.split()
junto=''.join(palavras)
inverso=junto[::-1]
# o fatiamento das letras do final que não sei usando o -1 para voltar
print('O inverso da frase é {}.'.format(inverso))
if inverso==junto:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase NÃO é um palíndromo!')
print('--FIM--')

