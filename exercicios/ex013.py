# dados = list()
# dados.append('Pedro')
# dados.append(25)
# # print(dados[0]) - Pedro
# # print(dados[1]) - 25

# pessoas = list()
# pessoas.append(dados[:])
# [:] - fatiamento / cópia dos elemtentos.

# pessoas = [['Pedro',25], ['Maria',19], ['João',32]] - lista dentro de lista.

# print(pessoas[0][0]) - dentro do item 0 (Pedro, 25) vai exibir apenas Pedro.
# print(pessoas[2][0]) - dentro do item 2 (João, 32) vai exibir apenas João.
# [:] - criar cópia

teste = list()
teste.append('Mario')
teste.append(34)
galera=list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
print(galera[0][0])
print(galera[1][1])
for p in galera:
    print(f'{p[0]} tem {p[1]} anos')

dado=list()
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
    # apago a lista dados 
print(galera)
totmai = totmen = 0
for p in galera:
    if p[1]>=21:
        print(f'{p[0]} é maior de idade')
        totmai+=1
    else:
        print(f'{p[0]} é menor de idade')
        totmen+=1
print(f'Temos {totmai} maior de idade e {totmen} menor de idade')