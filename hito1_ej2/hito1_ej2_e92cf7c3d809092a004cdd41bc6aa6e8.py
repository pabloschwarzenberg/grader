#Contestador de celular
numero = int(input("Favor ingrese el numero celular: "))
hora = int(input("Favor ingrese la hora: "))
numero_1 = str(numero)
dato_numero = (numero_1[5:8])


if hora>=0 and hora<=7:
    resultado = "CONTESTAR"
    print ("Resultado", resultado)
elif hora>7 and hora<=14 and dato_numero=="909":
    resultado = "CONTESTAR"
    print ("Resultado", resultado)
elif hora>7 and hora<=14:
        resultado = "NO CONTESTAR"
        print ("Resultado", resultado)
elif hora>14 and hora<=17:
    resultado = "NO CONTESTAR"
    print ("Resultado", resultado)
elif hora>17 and hora<=19 and dato_numero=="877":
    resultado = "CONTESTAR"
    print ("Resultado", resultado)
elif hora>17 and hora<=19:
    resultado = "NO CONTESTAR"
    print ("Resultado", resultado)
elif hora>19:
    resultado = "NO CONTESTAR"
    print ("Resultado", resultado)
else:
    print ("Rango de hora no valido")