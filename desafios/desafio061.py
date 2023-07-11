def leia_int(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Digite um valor inteiro válido')
            continue
        else:
            return n


def leia_float(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('Digite um valor float válido')
            continue
        else:
            return n


n_int = leia_int('Digite um valor inteiro: ')
print(f'O valor digitado foi {n_int}')
n_float = leia_float('Digite um valor float: ')
print(f'O valor digitado foi {n_float}')