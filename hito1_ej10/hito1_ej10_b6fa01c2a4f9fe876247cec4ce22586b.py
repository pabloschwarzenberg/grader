contador = 0
nuevoSaldoCajero = 1000000
nuevoSaldo = 100000

usuario = int(input("ingrese usuario: "))
contraseña = int(input("ingrese contraseña: "))

while (usuario != 10334151 and contraseña != 1803):

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

    if (monto.isdigit() == False and monto != "N" ):
        break

    if (int(monto) > nuevoSaldo or int(monto) > nuevoSaldoCajero):
        print("monto no permitido")
        break

    nuevoSaldo -= int(monto)
    nuevoSaldoCajero -= int(monto)

    print("saldo cuenta =",nuevoSaldo)
    print("saldo cajero =",nuevoSaldoCajero)