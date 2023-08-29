#Cajero Automático
#Entradas
saldo_cajero = 1000000
user = str(10334151)
password = str(1803)
saldo_user = 100000
intentos = 3
repeat = True
while repeat is True:
    x = input("Codigo de usuario: ")
    if x != user:
        print("Numero de usuario desconocido, porfavor intente de nuevo")
    else:
        while repeat is True:
            y = input("Contraseña: ")
            if y != password:
                print("Clave invalida")
                y = input("Contraseña: ")
                if y != password:
                    print("Clave invalida")
                    y = input("Contraseña: ")
                    if y != password:
                        print("Tarjeta Bloqueada")
                    else:
                        monto = int(input("Monto a retirar: "))
                        if monto > 100000:
                            print("Monto no permitido")
                        else:
                            cuenta = saldo_user - monto
                            cajero = saldo_cajero - monto
                            print("Saldo cuenta=", cuenta)
                            print("Saldo cajero=", cajero)

                else:
                    monto = int(input("Monto a retirar: "))
                    if monto > 100000:
                        print("Monto no permitido")
                    else:
                        cuenta = saldo_user - monto
                        cajero = saldo_cajero - monto
                        print("Saldo cuenta=", cuenta)
                        print("Saldo cajero=", cajero)
            else:
                monto = int(input("Monto a retirar: "))
                if monto > 100000:
                    print("Monto no permitido")
                else:
                    cuenta = saldo_user - monto
                    cajero = saldo_cajero - monto
                    print("Saldo cuenta=", cuenta)
                    print("Saldo cajero=", cajero)
            repeat = input("¿Dese usar el cajero de nuevo? Presione N si desea, si no, presione "
                           "cualquier otra tecla ")
            if repeat == "N":
                repeat = True
            else:
                repeat = False

