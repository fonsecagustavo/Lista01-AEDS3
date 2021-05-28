i = 0
listaNumeros = []
while i == 0:
    num = int(input("Digite um numero: "))
    listaNumeros.append(num)
    i = int(input("Para continuar digite 0, para sair qualquer outro valor: "))

print(listaNumeros)

def medida(lista):
    total = 0
    for i in lista:
        total += i
    total /= int(len(lista))

    return total

qtdElementos = medida(listaNumeros)

print("A media dos elementos e: " + str(qtdElementos))
