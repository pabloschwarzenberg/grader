#Cajero Automático
import sys
while True:
    U = eval(input("Ingrese el usuario: "))
    C = eval(input("Ingrese la clave: "))
    saldo_cajero = 1000000
    saldo_usuario = 100000
    if C == 1803:
        print("Clave válida")
        print("Saldo disponible: ", saldo_usuario)
    else:
        if C != 1803:
            print("Clave incorrecta")
            intento3 = int(input("Ingrese nuevamente la clave: "))
            if intento3 == 1803:
                print("Clave válida")
                print("Saldo disponible: ", saldo_usuario)
            else:
                print("Clave incorrecta,(Al proximo intento erróneo su tarjeta será bloqueada")
                intento3 = int(input("Ingrese nuevamente la clave: "))
                if intento3 != 1803:
                    print("Tarjeta bloqueada")
                    sys.exit()
                else:
                    print("Clave válida")
                    print("Saldo disponible: ", saldo_usuario)

    monto_retiro = eval(input("Ingrese el monto que desea retirar: "))
    if monto_retiro <= saldo_usuario:
        nuevo_saldo = saldo_usuario - monto_retiro
        saldo_cajero2 = saldo_cajero - monto_retiro
        print("Saldo cuenta = ", nuevo_saldo, )
        print("Saldo cajero =", saldo_cajero2)
    monto = monto_retiro
    billete_20000 = 0
    billete_10000 = 0
    billete_5000 = 0

    if monto >= 20000:
        billete_20000 = monto // 20000
        monto = monto - (billete_20000 * 20000)

    if monto >= 10000:
        Billete_10000 = monto // 10000
        monto = monto - (billete_10000 * 10000)

    if monto >= 5000:
        billete_5000 = monto // 5000
        monto = monto - (billete_5000 * 5000)
        
        print("\n")
        print("billetes 20000 = {0}".format(billete_20000))
        print("billetes 10000 = {0}".format(billete_10000))
        print("billetes 5000 = {0}".format(billete_5000))
    else:
        if monto_retiro > saldo_usuario:
            print("Monto no disponible")

    let = str(input("ingrese un digito distinto de N para salir: "))
    if let != "N":
        print("Gracias, hasta luego")
        break
      