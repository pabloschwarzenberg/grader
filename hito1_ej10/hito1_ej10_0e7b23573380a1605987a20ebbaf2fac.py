usuario = 10334151
clave = 1803
SI_cuenta = 100000
SI_cajero = 1000000

usuario_ingresado = int(input("Ingrese su usuario: "))
while True:

    contrasena_ingresada = int(input("Ingrese su contraseña: "))

    i = 0
    if i == 3:
        print("tarjeta bloqueada")
        break
    elif contrasena_ingresada != clave:
        print("clave invalida")
        i += 1
    if contrasena_ingresada == clave:
        monto_retirar = int(input("Ingrese monto a retirar: "))
        if isinstance(monto_retirar,float):
            print("monto no permitido")
        if isinstance(monto_retirar,int):
            NSI_cuenta = SI_cuenta - monto_retirar
            NSI_cajero = SI_cajero - monto_retirar
            print("saldo cuenta="+str(NSI_cuenta))
            print("saldo cajero="+str(NSI_cajero))
            break