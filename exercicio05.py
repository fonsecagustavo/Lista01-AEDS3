class Bomba :
    def __init__(self,tipo,valor,quantidade):
        self.tipo = tipo
        self.valor = valor
        self.quantidade = quantidade
    def abastecer_valor(self, valorAbastecidado):
        qtdLitros = valorAbastecidado / self.valor
        self.quantidade -= qtdLitros
        print("A quantidade de litros abastecida: " + str(qtdLitros) + "L")
    def abastecerLitros(self,litros):
        valorAdd = litros * self.valor
        self.quantidade -= litros
        print("O preço ficou: R$" + str(valorAdd))