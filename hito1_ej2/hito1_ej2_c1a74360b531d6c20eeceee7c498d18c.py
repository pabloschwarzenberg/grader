#Contestador de celular

while True:
    numero = int(input("Ingrese el numero telefonico: "))
    numstr = str(numero)

    if len(numstr) != 8:
        print("El numero ingresado no es valido.")

    else:
        hora = int(input("Ingrese la hora: "))

        if hora > 24 or hora < 0:
            print("La hora no esta correctamente ingresada.")

        else:
            break

numin = numstr[0:3]

if 0 <= hora <= 7:
    print("Resultado: CONTESTAR")

elif hora < 14 and numero % 1000 == 909:
    print("Resultado: CONTESTAR")

    if numero % 1000 != 909:
        print("Resultado: NO CONTESTAR")

elif 17 <= hora <= 19 and numin == "877":
    print("Resultado: NO CONTESTAR")

    if numin != "877":
        print("Resultado: CONTESTAR")

else:
    print("Resultado: NO CONTESTAR")
