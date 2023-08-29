#Cajero Automático
scajero = 1000000
scuenta = 100000
u = 10334151
c = 1803
bloq = 0
while True:
    usuario = int(input("ingrese usuario"))
    clave = int(input("ingrese clave"))
    if usuario == u:
        if clave != c:
            print("clave invalida")
            bloq = bloq + 1
            if bloq == 3:
                print("tarjeta bloqueada")
                break
            else:
                continue
        else:
            while True:
                monto = int(input("ingrese el monto a retirar"))
                if monto > scuenta:
                    print("monto no permitido")
                    salir = input("desea salir?")
                    if salir != "N":
                        break
                    else:
                        continue
                else:
                    scuenta = scuenta - monto
                    scajero = scajero - monto
                    print("saldo cuenta=" + str(scuenta))
                    print("saldo cajero=" + str(scajero))
                    salir = input("desea salir?")
                    if salir != "N":
                        break
                    else:
                        continue
    else:
        continue
    if salir != "N":
        break
    else:
        continue