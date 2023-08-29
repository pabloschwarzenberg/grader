saldo_cajero = 1000000
saldo_usuario = 100000
intentos = 0
while intentos < 3:
    usuario = int(input("Ingrese numero de usuario: "))
    clave = int(input("Ingrese su clave: "))

    if (usuario == 10334151):
        if(clave == 1803):
            dinero=int(input("Indique la cantidad de dinero que desea retirar: "))

            if (dinero>saldo_cajero):
                print("Monto no permitido")
                break
            elif (dinero>saldo_usuario):
                print("Monto no permitido")
                break
            elif (dinero<saldo_cajero):
                if (dinero<saldo_usuario):
                    saldo_usuario_nuevo = saldo_usuario-dinero
                    saldo_cajero_nuevo = saldo_cajero-dinero
                    print("Saldo cuenta=" ,saldo_usuario_nuevo)
                    print("Saldo cajero=",saldo_cajero_nuevo)
                    break
    elif (usuario != 10334151):
        if intentos == 2:
            print("Tarjeta Bloqueada")
            break
        else:
            print("Clave invalida")
            intentos = intentos+1
    elif (clave != 1803):
        if intentos == 2:
            print("Tarjeta Bloqueada")
            break
        else:
            print("Clave invalida")
            intentos = intentos+1
        
    intentos = intentos+1
    
            
