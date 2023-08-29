saldo_cajero = 1000000

usuario_real = "10334151"
clave_real = "1803"
saldo_usuario_real = 100000

intentos = 0
estado = True
while estado == True:

    usuario = input("Ingrese su usuario: ")
    clave = input("Ingresa la clave: ")

    if usuario == "N" or clave == "N":
        break

    if usuario == usuario_real and clave == clave_real:
        retiro_dinero = int(input("Monto de dinero a retirar: "))
        if retiro_dinero > saldo_usuario_real:
            print("Monto no permitido.")
        
        else:
            saldo_usuario_real = saldo_usuario_real - retiro_dinero
            saldo_cajero = saldo_cajero - retiro_dinero

            print("Saldo cuenta:", saldo_usuario_real)
            print("Saldo cajero:", saldo_cajero)

    elif clave != clave_real:
        print("Clave invalida.")
        intentos = intentos + 1
        if intentos == 3:
            print("Tarjeta bloqueada.")
            estado = False