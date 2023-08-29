#Cajero Automático
usuario = 10334151
clave = 1803
salir = "N"
while salir == "N":
    billetes20 = 0
    billetes10 = 0
    billetes5 = 0
    saldoCajero = 1000000
    saldoCuenta = 100000
    user = int(input("Ingrese usuario: "))
    if user==usuario:
        cont = 0
        while cont<3:
            passw = int(input("Ingrese clave de usuario: "))
            if passw!=clave:
                print("Clave inválida")
                cont += 1
            else:
                break
        if cont==3:
            print("Tarjeta bloqueada")
            break
        else:
            monto = 0
            flag = True
            while flag:
                monto = int(input("Ingrese monto a retirar: "))
                if monto<=100000:
                    saldoCuenta = saldoCuenta-monto
                    saldoCajero = saldoCajero-monto
                    print("saldo cuenta=",saldoCuenta)
                    print("saldo cajero=",saldoCajero)
                    if monto//20000>0:
                        billetes20 = monto//20000
                        monto = monto-(billetes20*20000)
                    else:
                        billetes20 = 0
                    if monto//10000>0:
                        billetes10 = monto//10000
                        monto = monto-(billetes10*10000)
                    else:
                        billetes10 = 0
                    if monto//5000>0:
                        billetes5 = monto//5000
                        monto = monto-(billetes5*5000)
                    else:
                        billetes5 = 0
                    print("billetes 20000=",billetes20)
                    print("billetes 10000=",billetes10)
                    print("billetes 5000=",billetes5)
                    flag = False
                else:
                    print("Monto no permitido")
    salir = input("Desea continuar: ")
    if salir!="N":
      break