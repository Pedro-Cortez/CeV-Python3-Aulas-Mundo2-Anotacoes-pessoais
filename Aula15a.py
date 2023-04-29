n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s = s + n
print('A soma é igual a {}.'.format(s))
print('A soma é igual a', s)
print(f'A soma vale {s}')
