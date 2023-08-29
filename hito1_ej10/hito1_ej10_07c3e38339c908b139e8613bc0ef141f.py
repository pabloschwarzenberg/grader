#Cajero Automático
usuario= int(input("Ingrese su usuario: "))
clave= int(input("Ingrese su clave: "))
saldoinicial=1000000
contadorintentos=1


while clave!=1803:
    if contadorintentos<3:
        print("clave invalida")
        contadorintentos= contadorintentos+1
        clave= int(input("Ingrese su clave: "))

    else:
        print("tarjeta bloqueada")
        break



while usuario==10334151 and clave==1803:
        saldousuario=100000
        montoaretirar= int(input("Ingrese el monto a retirar: "))

        if (saldousuario >= montoaretirar):
            saldocuenta = saldousuario - montoaretirar
            saldocajero= saldoinicial - montoaretirar
            print("saldo cuenta=",+saldocuenta)
            print("saldo cajero=",+saldocajero)
            deseacontinuar = input("Si desea continuar presione N")
            if deseacontinuar!='N':
                    break


        elif montoaretirar<0 or montoaretirar>saldousuario:
            print("monto no permitido ")      