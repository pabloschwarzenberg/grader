#Cajero Automático
saldo_cajero = 1000000
saldo_cuenta = 100000
clave = 1803
ingreso = int(input("Ingrese su clave: "))
continuar = True

if continuar:
    intentos = 1
    while intentos <= 3 and continuar:
        if ingreso == clave:
            retiro = int(input("Ingrese el monto a retirar: "))
            if retiro > saldo_cuenta:
                print("monto no permitido")
            else:
                saldo_cuenta = saldo_cuenta - retiro
                saldo_cajero = saldo_cajero - retiro
                print('saldo cuenta=', saldo_cuenta,'saldo cajero=', saldo_cajero)
                #seguir = str(input("Desea continuar (S/N): "))
                #if seguir == "N":
                #    continuar = False
        else:
            print("clave invalida")
            if intentos == 3:
                continuar = False
                print("tarjeta bloqueada")
        intentos += 1     