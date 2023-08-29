U = int(input("Usuario: "))
C = int(input("Clave: "))
dinero_total_cajero = 1000000
dinero_total_usuario = 100000
if U == 10334151 and C == 1803:
    monto = int(input("Monto a retirar: " ))
    X1 = dinero_total_cajero - monto
    X2 = dinero_total_usuario - monto
    if monto > 100000:
        print("monto no valido")
    else:
        print("saldo cuenta=",X2 ,", saldo cajero=",X1)
else:
    print("Clave invalida") 
    C = int(input("Introduzca nuevamente su clave: "))
    if C == 1803:
        monto = int(input("Monto a retirar: " ))
        X1 = dinero_total_cajero - monto
        X2 = dinero_total_usuario - monto
        if monto > 100000:
            print("monto no valido")
        else:
            print("saldo cuenta=",X2 ,", saldo cajero=",X1)
    else:
        print("Clave invalida") 
        C = int(input("Introduzca nuevamente su clave: "))
        if C == 1803:
            monto = int(input("Monto a retirar: " ))
            X1 = dinero_total_cajero - monto
            X2 = dinero_total_usuario - monto
            if monto > 100000:
                print("monto no valido")
            else:
                print("saldo cuenta=",X2 ,", saldo cajero=",X1)
        else:
            print("Tarjeta Bloqueada")