def cajero():
    saldo_cajero = 1000000
    saldo_cuenta = 100000
    intentos = 0

    while True:
        
        usuario_valido = 10334151
        clave_valida = 1803

        usuario = int(input("Ingrese su usuario: "))
        clave = int(input("Ingrese su clave: "))

        if usuario == usuario_valido and clave == clave_valida:
        
            while True:
                monto = int(input("ingresa el monto que desea retirar: "))

                if monto > saldo_cuenta:
                    print("Monto no permitido.")
                else:
                    saldo_cuenta -= monto
                    saldo_cajero = saldo_cajero - saldo_cuenta
                    print("Saldo cuenta =", saldo_cuenta)
                    print("Saldo cajero =", saldo_cajero)

                continuar = input("¿Desea realizar otra transacción? (N para salir): ")
                if continuar.upper() == "N":
                    break
        else:
            intentos += 1
            if intentos == 3:
                print("Tarjeta bloqueada." , intentos, "de 3")
                break
            else:
                print("Clave inválida.", intentos, "de 3")

       
cajero()