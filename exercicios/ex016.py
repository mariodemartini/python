try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Você não digitou um numero')
except ZeroDivisionError:
    print('Você colocou 0 (ZERO) no denominador') 
except Exception as erro: 
    print(f'ERRO! Algum número não é aceito. {erro.__cause__}')
# except Exception as erro: EXCEPTION GENERICA
#     print(f'ERRO! Algum número não é aceito. {erro.__class__}')
else:
    print('O resultado é: ', r)
finally:
    print('Tente mais vezes')
    