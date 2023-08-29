#Cajero Automatico

saldo_cajero = 1000000
saldo_usuario = 100000
suma = 0
billetes20 = 20
billetes10 = 40
billetes5 = 40
cant20 = 0
cant10 = 0
cant5 = 0
confirmacion = False
usuario = input("Ingrese usuario: " )
while True:
    if usuario == "10334151":
        clave = input("ingrese clave: ")
        if clave == "1803":
            retiro = int(input("Monto a retirar: "))
            if 0 < retiro < saldo_usuario:
                confirmacion = True
                saldo_cuenta = saldo_usuario - retiro
                saldo_cajero_final = saldo_cajero - retiro
                print("saldo cuenta=",saldo_cuenta)
                print("saldo cajero=",saldo_cajero_final)
                break
            else:
                print("monto no permitido")
                break
        else:
            if suma == 2:
                print("tarjeta bloqueada")
                break
            else:
                print("clave invalida")
                suma += 1
    else:
        usuario = input("Ingrese usuario: " )

if confirmacion == True:
    while True:
        if retiro >= 20000:
            cant20 += 1
            retiro -= 20000
        else:
            if retiro >= 10000:
                cant10 += 1
                retiro -= 10000
            else:
                if retiro >= 5000:
                    cant5 += 1
                    retiro -= 5000
        if retiro == 0:
            saldo_cuenta = saldo_usuario - retiro
            saldo_cajero_final = saldo_cajero - retiro
            print("billetes 20000=",cant20)
            print("billetes 10000=",cant10)
            print("billetes 5000=",cant5)
            break

