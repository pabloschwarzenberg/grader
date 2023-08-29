saldo = 1000000
saldoC = 100000
usuario= int(input("Ingrese el Número de Usuario: "))
clave = int(input("Ingrese la clave: "))
intentos = 0

while usuario == 10334151:
    try:
        if clave != 1803:
            intentos = intentos +1
            print("clave invalida")
            clave = int(input("Ingrese la clave: "))
            if intentos == 2:
                print("tarjeta bloqueada")
                break
        else:
            if clave == 1803:
                plata = int(input("Ingrese el monto a retirar: "))
            if plata <= 100000:
                dinero = saldoC - plata
                pcajero = saldo - plata
                print("saldo cuenta=",dinero)
                print("saldo cajero=", pcajero)
            else:
                print("Monto no permitido")
                continue
    except ValueError:
        break