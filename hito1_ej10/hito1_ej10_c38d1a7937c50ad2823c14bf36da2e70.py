#Cajero Automático
usuario = 10334151
clave = 1803
saldocajero = 1000000
saldocuenta = 100000
intento = 0
repetir = 0
print("Bienvenido!")
print("Saldo cajero-> ", saldocajero)
op = int(input("Que desea hacer? \n1) Ingresar \n2) Salir \n-> "))
if op != 2:
    while repetir != 100:
        while intento < 3:
            op = str(input("Que desea hacer? \n1) Retirar dinero \n2) Salir \n-> "))
            if op != 2:
                print("Usuario -> ", usuario)
                password = str(input("Ingrese clave -> "))
                if password == clave:
                    retiro = float(input("Ingrese monto a retirar -> "))
                    if retiro <= 100000:
                        saldocuenta -= retiro
                        saldocajero -= retiro
                        print("Saldo cuenta = ",saldocuenta)
                        print("Saldo cajero = ",saldocajero)
                    else:
                        print("Monto no permitido")
                else:
                    print("Clave invalida")
                    intento += 1
                repetir += 3
            else:
                exit()
        if intento == 3:
            print("Tarjeta bloqueada")
            exit()
else:
    exit()