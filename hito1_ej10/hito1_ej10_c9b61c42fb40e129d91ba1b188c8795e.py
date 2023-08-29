#Cajero Automático
usuario = 10334151
clave = 1803
salir = "N"
while salir == "N":
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
                    flag = False
                else:
                    print("Monto no permitido")
    salir = input("Desea continuar: ")
    if salir!="N":
      break