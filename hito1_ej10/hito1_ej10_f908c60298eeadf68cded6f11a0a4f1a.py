from time import sleep
x = 1000000
y = 100000
usuario = str(int(input("Ingrese el usuario: ")))
contrasena = str(int(input("Ingrese la contraseña: ")))
while True:
    if usuario == "10334151" and contrasena == "1803":
        print("Usuario y contraseña correctos")
        sleep(1)
        monto_a_retirar = int(input("Ingrese el monto a retirar: "))
        if monto_a_retirar>y and monto_a_retirar>x:
            print("monto no permitido")
            break
        if monto_a_retirar<y and monto_a_retirar<x:
            y_final = y-monto_a_retirar
            x_final = x-monto_a_retirar
            print("saldo cuenta=", y_final)
            print("saldo cajero=", x_final)
        if monto_a_retirar!="N":
            break
    if usuario != "10334151" or contrasena != "1803":
        print("clave invalida")
        sleep(1)
        print("INTENTO N°2")
        sleep(1)
        contrasena = str(int(input("Ingrese la contraseña denuevo: ")))
        if usuario != "10334151" or contrasena != "1803":
            print("clave invalida")
            sleep(1)
            print("INTENTO N°3")
            sleep(1)
            contrasena = str(int(input("Ingrese la contraseña denuevo: ")))
            if usuario != "10334151" or contrasena != "1803":
                print("tarjeta bloqueada")
                break