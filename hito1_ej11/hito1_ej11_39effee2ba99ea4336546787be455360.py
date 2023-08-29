cuentas = {"10769042": [100000, "1803"], "10334151": [100000, "1803"], "55555555": [43000, "Abc123"]}
def billetes (monto_1):
    VM=20000
    DM=10000
    CM=5000
    billetes_20000=0
    billetes_10000=0
    billetes_5000=0

    while monto_1>0:
        if monto_1//VM>0:
            billetes_20000=monto_1//VM
            monto_1-=(billetes_20000)*20000
            print("billetes 20000=", (billetes_20000))
        elif monto_1//DM>0:
            billetes_10000=monto_1//DM
            monto_1-=(billetes_10000)*10000
            print("billetes 10000=", (billetes_10000))
        elif monto_1//CM>0:
            billetes_5000=monto_1//CM
            monto_1-=(billetes_5000)*5000
            print("billetes 5000=", (billetes_5000))
        else:
            print("No hay billetes para repartir",(monto_1))
            monto_1-=monto_1
# ACCEDER Y VALIDAR CUENTA Y CLAVE
sistema=True
user = 0
num = 0
lukas = 0
error = 0
cajero = 1000000
achuntale = False
salida = False

while not salida:
    num = 0
    error = 0

    achuntale = False

    while not achuntale:
        if error > 2:
            print("tarjeta bloqueada")
            achuntale = True

        else:
            if error < 1:
                user = (input("ingrese su usuario:"))
                

                if user in cuentas:
                    clave = (input("ingrese su clave:"))
                    num = (cuentas[user][1])
                    lukas = int(cuentas[user][0])
                    if clave == num:
                        print("ok")
                        achuntale = True

                    else:
                        print("clave invalida")
                        error += 1

                else:
                    print("usuario inexistente")
                    break
            else:
                clave = (input("ingrese su clave:"))
                if user in cuentas:
                    num = (cuentas[user][1])
                    lukas = int(cuentas[user][0])
                    if clave == num:
                        print("ok")
                        achuntale = True
                    else:
                        print("clave invalida")
                        error += 1

                else:
                    print("usuario inexistente")
                    sistema=False


    # RETIRAR DINERO
    if sistema==True:
        monto = int(input("ingresa el monto a retirar:\n"))
        if monto > lukas:
            print("monto no permitido")

        else:
            billetes(monto)
            lukas -= monto
            cuentas[user][0] -= monto

            cajero -= monto
            print("saldo cuenta=",(lukas))
            print("saldo cajero=",(cajero))

            print("quieres salir? Y/N")
            salida = input("")
            if salida != "N":
                salida = True
            else:
                salida = False
    else:
        print("quieres salir? Y/N")
        salida = input("")
        if salida != "N":
            salida = True
        else:
            salida = False
      
      