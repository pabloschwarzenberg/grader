# usuario = 10334151
# contraseña =  1803
contador = 0
nuevoSaldoCajero = 1000000
nuevoSaldo = 100000
veinte = 20
diez = 40
cinco = 40

usuario = int(input("ingrese usuario: "))
contraseña = int(input("ingrese contraseña: "))

while (usuario != 10334151 or contraseña != 1803):

    if (contador == 2):
        print("tarjeta bloqueada")
        break

    if (usuario != 10334151):
        contador += 1
        print("clave invalida")

    usuario = int(input("ingrese usuario: "))
    contraseña = int(input("ingrese contraseña: "))

while (usuario == 10334151 and contraseña == 1803):

    monto = input("ingrese monto a retirar: ")

    if (monto.isdigit() == False and monto != "N"):
        break

    if ((float(monto) / 20000) % 1 * 100) == 25:
        veinte-= int(monto)/20000
        cinco -= 1
        print("billetes 20000 = ", round(int(monto)/20000))
        print("billetes 5000 = ", 1)

    elif ((float(monto) / 20000) % 1 * 100) == 75:
        veinte -= int(monto) / 20000
        diez-= int(monto)/20000
        cinco -= 1
        print("billetes 10000= ",1)
        print("billetes 20000 = ", int(int(monto)/20000))
        print("billetes 5000 = ", 1)

    elif ((float(monto) / 20000) % 1 * 100) == 50:
        veinte -= int(monto) / 20000
        diez-= int(monto)/20000
        print("billetes 10000= ",1)
        print("billetes 20000 = ", int(int(monto)/20000))

    elif ((float(monto) / 20000) % 1 * 100) == 0:
        veinte -= int(monto) / 20000
        print("billetes 20000 = ", int(int(monto)/20000))

    else:
        print("Monto invalido")



    if (int(monto) > nuevoSaldo or int(monto) > nuevoSaldoCajero):
        print("monto no permitido")
        break

    nuevoSaldo -= int(monto)
    nuevoSaldoCajero -= int(monto)

    print("saldo cuenta=",nuevoSaldo)
    print("saldo cajero=",nuevoSaldoCajero)