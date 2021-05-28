i = 0
listaNumeros = []
while i == 0:
    num = int(input("Digite um numero para a lista: "))
    listaNumeros.append(num)
    i = int(input("Para continuar digite 0, para sair qualquer outro valor: "))

print("--------")
num = int(input("Digite um numero para busca: "))

def index(lista,numero):
    i = 0
    while i < len(lista):
        if lista[i] == numero:
            return i
        i += 1

    return -1

qtdElementos = index(listaNumeros,num)

if qtdElementos != -1:
    print("index: " + str(qtdElementos))
else:
    print('Numero não encontrado')