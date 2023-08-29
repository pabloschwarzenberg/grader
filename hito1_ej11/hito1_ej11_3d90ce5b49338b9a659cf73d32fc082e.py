#Cajero Automático

#Credenciales
usuarios = [103341561]
claves = [1803]

#Saldos
saldoCaja = [1000000]
saldoCuentas = [100000]
intentos = 3
montoRetirado = ""

#Billetes
vBilletes = [20000,10000,5000]
cBilletes = [20,40,40]
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
        print("Su vuelto en detalle es de: ")
        if(aRetirar//vBilletes[0] != 0):
            cBilletes[0] = cBilletes[0] - (aRetirar//vBilletes[0])
            print("billetes 20000=" + str(aRetirar // vBilletes[0]))
            aRetirar = aRetirar % vBilletes[0]

        if (aRetirar // vBilletes[1] != 0):
            cBilletes[1] = cBilletes[1] - (aRetirar // vBilletes[1])
            print("billetes 10000=" + str(aRetirar // vBilletes[1]))
            aRetirar = aRetirar % vBilletes[1]

        if (aRetirar // vBilletes[2] != 0):
            cBilletes[2] = cBilletes[2] - (aRetirar // vBilletes[2])
            print("billetes 5000=" + str(aRetirar // vBilletes[2]))
            aRetirar = aRetirar % vBilletes[2]
