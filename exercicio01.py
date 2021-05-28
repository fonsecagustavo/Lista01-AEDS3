valor = float(input('Salario que ganha:'))

def calculo_imposto():
        if valor <= 1903.99:
                imposto = 0
        elif valor <= 2826.66:
                imposto = valor * 0.075
        elif valor <= 3751.05:
                imposto = valor * 0.15
        elif valor <= 4664.68:
                imposto = valor * 0.225
        else:
                imposto = valor * 0.275
        return imposto

serPago = calculo_imposto()

print('Imposto a ser pago pelo salario: ')
print('Salario: ' + str(valor))
print('Imposto: '+ str(serPago))
