#Cajero Automático
saldo_inicial = 1000000
saldo = 0
usuario = int(input("mencione su rut sin digito verificador por favor: "))
clave = int(input("ingrese su clave de 4 digitos por favor: "))
saldo_usuario = 100000
intentos = 3
while intentos != 0:
    if clave != 1803:
        for i in range(1, intentos+1):    
            if clave != 1803:   
                intentos = intentos - 1
                print("Su clave no es correcto, tiene ", intentos+1, "intentos")
                print("intentelo de nuevo")
                clave = int(input("ingrese su clave de 4 digitos: "))
    elif intentos == 0:
        print("tarjeta bloqueada")
        break

    else:
            clave = True
            monto_a_sacar = int(input("ingrese el monto a sacar por favor: "))
            if monto_a_sacar > saldo_usuario or monto_a_sacar < 0:
                print("monto no permitido")
                monto_a_sacar = int(input("ingrese el monto a sacar por favor: "))
                continue
            else:
                monto_que_sobra = saldo_usuario - monto_a_sacar
                print("saldo cuenta=", monto_que_sobra)
                print("saldo cajero=", saldo_inicial - monto_a_sacar )
                break