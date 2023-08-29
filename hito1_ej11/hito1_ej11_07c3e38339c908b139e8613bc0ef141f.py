#Cajero Automático
usuario= int(input("Ingrese su usuario: "))
clave= int(input("Ingrese su clave: "))
saldoinicial=1000000
contadorintentos=1
billetes20=20
billetes10=40
billetes5=40

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


            cantidadbilletes20= montoaretirar//20000
            restantes20= montoaretirar%20000

            if restantes20 == 0:
                print("billetes 20000=", +cantidadbilletes20)

            else:
                cantidadbilletes10 = restantes20 // 10000
                restantes10 = restantes20 % 10000
                if restantes10 == 0:
                    print("billetes 20000=", +cantidadbilletes20)
                    print("billetes 10000=", +cantidadbilletes10)
                else:
                    cantidadbilletes5= restantes10//5000
                    print("billetes 20000=", +cantidadbilletes20)
                    print("billetes 10000=", +cantidadbilletes10)
                    print("billetes 5000=", +cantidadbilletes5)



            deseacontinuar = input("Si desea continuar presione N")
            if deseacontinuar!='N':
                    break


        elif montoaretirar<0 or montoaretirar>saldousuario:
            print("monto no permitido ")