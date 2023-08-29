usuario= int(input("Usuario: "))

    # verificar datos antes de empezar transacciones
if (usuario != 10334151):
        print("Nombre de usuario no identificado.")
else:
    clave = int(input("Clave: "))
    if (clave != 1803):
        print("Clave invalida. Intente nuevamente, tienes dos oportunidades mas para ingresarla correctamente.")
        for i in range(0, 2):
            clave = int(input("Clave: "))
            if (i == 0 and clave != 1803):
                print("Clave invalida. Intente una vez mas.")
            elif (i == 1 and clave != 1803):
                print("Clave invalida. Tarjeta bloqueada.")
            else:
                print("Usuario y clave aceptada.")
                break

    # input monto a retirar

monto = float(input("Ingrese un monto a retirar: "))
saldo = float(100000)
cajero = float(1000000)

if (monto > saldo):
    print("Monto no permitido, excede su saldo actual.")
else:
    saldo = saldo - monto
    cajero = cajero - monto
    print("saldo cuenta= " + str(saldo))
    print("saldo cajero= " + str(cajero))