def descomposicion_numeros(numero):
    unidades = numero % 10
    decenas = (numero // 10) % 10
    centenas = (numero // 100) % 10
    miles = numero // 1000

    descomposicion = []

    if miles > 0:
        descomposicion.append(str(miles) + "M")
    if centenas > 0:
        descomposicion.append(str(centenas) + "C")
    if decenas > 0:
        descomposicion.append(str(decenas) + "D")
    if unidades > 0:
        descomposicion.append(str(unidades) + "U")

    resultado = "+".join(descomposicion)
    print(resultado)


numero = int(input("Ingrese un número de hasta 4 dígitos: "))
descomposicion_numeros(numero)
