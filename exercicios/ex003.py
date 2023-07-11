n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
s = n1 + n2
d = n1 / n2
m = n1 * n2
e = n1 ** n2
di = n1 // n2
r = n1 % n2
print('O resultado da soma é {},\nO resultado da divisão é {},\nO resultado da multiplicação é {},'.format(s, d, m))
print('O resultado da potência é {:5},\nA divisão inteira é {},\nO resto da divisão é {}.'.format(e, di, r))
