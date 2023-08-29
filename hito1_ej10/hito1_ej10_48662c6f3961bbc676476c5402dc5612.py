#Cajero Automático
cajero = 1000000
cuenta = 100000

usuario = input("Usuario: ")

monto = 1000001
salida = "N"
seguridad = 0
while salida == "N":
    while seguridad != 3:
        clave = input("Clave: ")
        if clave != "1803":
            print("Clave inválida")
            seguridad += 1

            if seguridad == 3:
                print("Tarjeta bloqueada")
                salida = "S"

        else:
            break

    while salida == "N" and seguridad != 3:
        monto = int(input("Monto a retirar: "))
        if monto > cuenta:
            print("Monto no permitido")

        else:
            cajero -= monto
            cuenta -= monto

            print("Saldo cuenta={}".format(cuenta))
            print("Saldo cajero={}".format(cajero))

            salida = input("¿Salir? S/N: ")