#Cajero Automático
usuarios = [103341561]
claves = [1803]
saldoCaja = [1000000]
saldoCuentas = [100000]
intentos = 3
control = True
while control:
    while intentos != 0:
        uss = input("Ingrese usuario: ")
        ky = input("Ingrese clave: ")
        if (uss != "N" or ky != "N"):
            control = False
            break
        else:
            user = int(uss)
            key = int(ky)
        if (user == usuarios[0] and key == claves[0]):
            print("Bienvenido")
            break
        else:
            print("Usuario o clave incorrectos, ingrese nuevamente")
            intentos = intentos - 1
            if (intentos == 0):
                print("Tarjeta bloqueada")
                sys.exit()
    aRetirar = int(input("Ingrese el monto a retirar: "))
    if (aRetirar > saldoCuentas[0]):
        print("Monto no valido, realice nuevamente la operacion")
    else:
        saldoCuentas[0] = saldoCuentas[0] - aRetirar
        saldoCaja[0] = saldoCaja[0] - aRetirar
        print("saldo cuenta=", str(saldoCuentas[0]))
        print("saldo cajero=", str(saldoCaja[0]))      