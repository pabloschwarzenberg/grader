#Cajero Automático
cajero = 1000000
saldo = 100000
usuario = int(int(input("Ingrese el usuario: ")))
codigo = int(int(input("Ingrese la contraseña: ")))
while True:
    if usuario == 10334151 and codigo == 1803:
        print("Usuario y contraseña correctos")
        monto = int(input("Ingrese el monto a retirar: "))
        if monto > saldo and monto > cajero:
            print("monto no permitido")
            break
        if monto < saldo and monto < cajero:
            saldo_final = saldo - monto
            cajero_final = cajero - monto
            print("saldo cuenta=", saldo_final)
            print("saldo cajero=", cajero_final)
        if monto!= "N":
            break
    if usuario != 10334151 or codigo != 1803:
        print("clave invalida")
        print("INTENTO N°2")
        codigo = str(int(input("Ingrese la contraseña denuevo: ")))
        if usuario != 10334151 or codigo != 1803:
            print("clave invalida")
            print("INTENTO N°3")
            codigo = str(int(input("Ingrese la contraseña denuevo: ")))
            if usuario != 10334151 or codigo != 1803:
                print("tarjeta bloqueada")
                break