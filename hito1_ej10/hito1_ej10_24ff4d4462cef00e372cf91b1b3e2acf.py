user= int(input("ingrese el numero de usuario:"))
clave= int(input("ingrese la clave de 4 digitos:"))
saldo_base= 100000

if clave == 1803:
    print("clave valida")
    print("su saldo es:", saldo_base)
    retiro = int(input("ingrese la cantidad que desea retirar:"))
    res= 100000 - retiro
    cajero= 1000000 - retiro
    if res <= 100000:
        print("saldo cuenta=", res)
        print("saldo cajero=", cajero)
    else:
        print("monto no disponible")
else:
    if clave != 1803:
        print("clave invalida")

    a= int(input("inserte clave nuevamente:"))
    if a == 1803:
        print("clave valida")
        print("su saldo es de:", saldo_base)
        retiro = int(input("ingrese la cantidad que desea retirar:"))
        resta = 100000 - retiro
        cajero = 1000000 - retiro
        if resta <= 100000:
            print("saldo cuenta=", res)
            print("saldo cajero=", cajero)
        else:
            print("monto no disponible")
    else:
        if a != 1803:
            print("clave  invalida")
        b = int(input("ingrese clave nuevamente:"))
        if b == 1803:
            print("clave valida")
            print("su saldo es de:", saldo_base)
            retiro = int(input("ingrese la cantidad que desea retirar:"))
            res = 100000 - retiro
            cajero = 1000000 - retiro
            if resta <= 100000:
                print("saldo cuenta=", res)
                print("saldo cajero=", cajero)
            else:
                print("monto no disponible")
        else:
            if b!=1803:
                print("tarjeta bloqueada")
while True:
    orden = str(input("ingrese algo direfente a N para salir:"))
    if orden != "N":
        print("borrar memoria....")
        break