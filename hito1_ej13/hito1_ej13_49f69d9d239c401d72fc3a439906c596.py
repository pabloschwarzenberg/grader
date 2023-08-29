numero = int(input('Ingrese su numero: '))
denominador = 2

while denominador <= numero:
    if numero % denominador == 0:
        print(denominador)
        numero /= denominador
    else:
        denominador += 1