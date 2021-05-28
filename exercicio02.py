n = int(input('Valor: '))
aux = n - 2
i = 0
while i < n:
    if i == 0 or i == n-1:
        print('*' * n)

    else:
        print('*' + ' ' * aux + '*')

    i += 1
