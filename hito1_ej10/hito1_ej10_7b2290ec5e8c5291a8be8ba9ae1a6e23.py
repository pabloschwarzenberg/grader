import time

def ingresar():
    saldo_cajero = 1000000
    saldo_cuenta = 100000

    usuario = int(input("Ingrese su usuario: "))
    clave = int(input("Ingrese su clave: "))

    counter = 0
    while clave != 1803:
        counter = counter + 1

        if counter == 3:
            print("tarjeta bloqueada")
            time.sleep(2)
            quit()

        print("clave invalida")
        clave = int(input("Ingrese su clave: "))

    if clave == 1803:
        print("Ingresaste a tu cuenta!")


        y_n = True
        while y_n:
            monto_retiro = input("Ingrese monto a retirar: ")

            if int(monto_retiro) <= saldo_cuenta and int(monto_retiro) > 0:
                saldo_cajero = saldo_cajero - int(monto_retiro)
                saldo_cuenta = saldo_cuenta - int(monto_retiro)
                print("saldo cuenta=" + str(saldo_cuenta))
                print("saldo cajero=" + str(saldo_cajero))


            else:
                print("monto no permitido")
                monto_retiro = input("Ingrese monto a retirar: ")

            salir = input("Ingrese alguna letra distinta de N para salir ")

            if salir.upper() != "N":
                y_n = False


ingresar()