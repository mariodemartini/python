import moeda

p = moeda.leia_dinheiro('Informe o preço: R$')
t = moeda.leia_taxa('Informe a taxa(%): ')
moeda.resumo(p, t)