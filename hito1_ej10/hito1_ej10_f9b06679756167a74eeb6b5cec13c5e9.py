while True:
    usuario=int(input("ingrese su usuario: "))
    clave= int(input("ingrese su clave: "))
    saldo_cajero=1000000
    saldo_usuario=100000
    if clave==1803:
        print("clave valida")
        print("saldo disponible", saldo_usuario)
        monto_a_retirar= int(input("ingrese el monto a retirar: "))
        if monto_a_retirar<=100000:
            saldo_usuario_2= int(100000 - monto_a_retirar)
            print("saldo cuenta= ", saldo_usuario_2)
            saldo_actual= int(1000000 - monto_a_retirar)
            print("saldo cajero= ", saldo_actual)
            salir=input("ingrese algo distinto de N para salir:")
            if salir=="N":
                continue
            else:
                break
        elif monto_a_retirar>100000:
            print("monto no permitido")
        
    else:
        if clave!=1803:
            print("clave invalida")
            intento2=int(input("ingrese su clave: "))
            if intento2==1803:
                print("clave valida")
                print("saldo disponible:", saldo_usuario)
                monto_a_retirar= int(input("ingrese el monto a retirar: "))
                if monto_a_retirar<=100000:
                    saldo_usuario_2= int(100000 - monto_a_retirar)
                    print("saldo cuenta= ", saldo_usuario_2)
                    saldo_actual= int(1000000 - monto_a_retirar)
                    print("saldo cajero= ", saldo_actual)
                    salir=input("ingrese algo distinto de N para salir:")
                    if salir=="N":
                        continue
                    else:
                        break
                elif monto_a_retirar>100000:
                    print("monto no permitido")
                    break
            
            else:
                if intento2!=1803:
                    print("clave invalida")
                    intento3=int(input("ingrese su clave: "))
                    if intento3==1803:
                        print("clave valida")
                        print("saldo disponible:",saldo_usuario)
                        monto_a_retirar= int(input("ingrese el monto a retirar: "))
                        if monto_a_retirar<=100000:
                            saldo_usuario_2= int(100000 - monto_a_retirar)
                            print("saldo cuenta= ", saldo_usuario_2)
                            saldo_actual= int(1000000 - monto_a_retirar)
                            print("saldo cajero= ", saldo_actual)
                            salir=input("ingrese algo distinto de N para salir:")
                            if salir=="N":
                                continue
                            else:
                                break
                        elif monto_a_retirar>100000:
                            print("monto no permitido")
                            break
                else:
                    print("tarjeta bloqueada")
                    break
                    
