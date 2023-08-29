#Cajero Automático
#Datos
usuario = 10334151
contraseña = 1803
cajero_cash = 1000000
usuario_cash = 100000

#Procesos

user_in = int(input("Ingrese número de usuario: "))
if user_in == usuario:
    pass_1 = int(input("Ingrese contraseña: "))
    if pass_1 == contraseña:
        retiro = int(input("Ingrese monto a retirar:$ "))
        if retiro <= 100000:
            print("saldo cuenta=",(usuario_cash - retiro))
            print("saldo cajero=",(cajero_cash - retiro))
        else:
            print("monto no permitido")
        
    elif pass_1 != contraseña:
        print("clave invalida")
        pass_2 = int(input("Ingrese contraseña: "))
        if pass_2 == contraseña:
            retiro = int(input("Ingrese monto a retirar:$ "))
            if retiro <= 100000:
                print("saldo cuenta=",(usuario_cash - retiro))
                print("saldo cajero=",(cajero_cash - retiro))
            else:
                print("monto no permitido")

        elif pass_2 != contraseña:
            print("clave invalida")
            pass_3 = int(input("Ingrese contraseña: "))
            if pass_3 == contraseña:
                retiro = int(input("Ingrese monto a retirar:$ "))
                if retiro <= 100000:
                    print("saldo cuenta=",(usuario_cash - retiro))
                    print("saldo cajero=",(cajero_cash - retiro))
                else:
                    print("monto no permitido")
            
            else: print("tarjeta bloqueada")
        
else:print("usuario incorrecto")