#Cajero Automático
Usuario = eval(input("Ingrese su usuario:"))
Clave = eval(input("Ingrese su clave:"))


IngresoCajero = 1000000
Monto1803 = 100000

if Usuario != 10334151:
    print("Usuario no registrado")

else:

    if Clave != 1803:
        print("Clave no válida")
        Clave = eval(input("Ingrese su clave nuevamente:"))
        
        if Clave != 1803:
            print("Clave no válida")
            Clave = eval(input("Ingrese su clave nuevamente:"))

            if Clave != 1803:
                print("Tarjeta bloqueada")

            else:
                x = eval(input("Ingrese monto a retirar:"))
                print("saldo cuenta=", Monto1803 - x)
                print("saldo cajero=", IngresoCajero - x)
                

        else:

            x = eval(input("Ingrese monto a retirar:"))
            print("saldo cuenta=", Monto1803 - x)
            print("saldo cajero=", IngresoCajero - x)

    else:
        x = eval(input("Ingrese monto a retirar:"))
        print("saldo cuenta=", Monto1803 - x)
        print("saldo cajero=", IngresoCajero - x)