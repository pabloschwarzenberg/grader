#Cajero Automático
usuario = 10334151
contrasena = 1803

saldo_cajero = 1000000
saldo_usuario= 100000

def retirar_dinero(d, su, sc):
    if d > su:
        print("monto no permitido")
    else:
        print("saldo cuenta=" + str((su-d)))
        print("saldo cajero=" + str((sc-d)))

usuario_ingresado= int(input("Ingresa tu usuario:"))
contrasena_ingresada=int(input("Ingresa tu contraseña:"))

if contrasena == contrasena_ingresada:
    retirar_dinero(int(input("Cuanto dinero deseas retirar:")), saldo_usuario, saldo_cajero)
else:
    contrasena_ingresada=int(input("Ingresa tu contraseña:"))
    if(contrasena_ingresada == contrasena):
        retirar_dinero(int(input("Cuanto dinero deseas retirar:")), saldo_usuario, saldo_cajero)
    else:
        contrasena_ingresada=int(input("Ingresa tu contraseña:"))
        if(contrasena_ingresada == contrasena):
            retirar_dinero(int(input("Cuanto dinero deseas retirar:")), saldo_usuario, saldo_cajero)
        else:
            print("tarjeta bloqueada")      