import math
n = float(input('Digite qualquer número: '))
i = math.trunc(n)
print('A parte inteira de {} é {}'.format(n, i))

print('-'*25)

catop = float(input('Qual a medida do cateto oposto: '))
catad = float(input('Qual a medida do cateto adjacente: '))
hip = math.hypot(catop, catad)
print('A hipotenusa vai medir {:.2f}'.format(hip))

print('-'*25)

ang = float(input('Digite um ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tg = math.tan(math.radians(ang))
print('O seno é {:.3f}\nO cosseno é {:.3f}\nA tangente é {:.3f}'.format(sen, cos, tg))

print('-'*25)



