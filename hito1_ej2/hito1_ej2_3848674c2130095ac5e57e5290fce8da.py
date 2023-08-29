#Contestador de celular
numero = int(input("Ingrese numero de telefono: "))
hora = int(input("Ingrese hora de la llamada: "))


if hora >= 0 and hora <= 7:
    resultado = "CONTESTAR"
elif hora > 7 and hora < 14: 
    if numero % 1000 != 909:
        resultado = "NO CONTESTAR"
    else:
        resultado = "CONTESTAR"
elif hora >= 14 and hora < 17:
    resultado = "NO CONTESTAR"
elif hora >= 17 and hora <= 19:
    if numero // 100000 != 877:
        resultado = "CONTESTAR"
    else:
        resultado = "NO CONTESTAR"
elif hora > 19 and hora < 24:
    resultado = "NO CONTESTAR"

if hora >= 24 or hora < 0 or len(str(numero)) != 8:
    resultado = "NUMERO INCORRECTO"

print(resultado)