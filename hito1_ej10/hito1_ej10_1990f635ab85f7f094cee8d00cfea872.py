#Cajero Automático
Usuario = 10334151
Clave = 1803
Saldo_Cuenta = 100000
Saldo_Cajero = 1000000
Intentos = 3
print("Banco RobaChile, tu dinero, nuestro dinero :D ")
print("Indique su usuario y su clave...")
Usuario = int(input("Usuario: "))
Clave = int(input("Clave de ingreso: "))
if Usuario == 10334151 and Clave == 1803:
    print("Saldo Cuenta =", Saldo_Cuenta)
    print("Saldo Cajero =", Saldo_Cajero)
    Retiro = int(input("¿Cuanto dinero quiere retirar?: "))
    if Retiro < Saldo_Cuenta and Saldo_Cajero:
        Resta_Cuenta = Saldo_Cuenta - Retiro
        Resta_Cajero = Saldo_Cajero - Retiro
        print("¡Retiro con exito! Su saldo en nuestro banco es: ")
        print("Saldo Cuenta =", Resta_Cuenta)
        print("Saldo Cajero =", Resta_Cajero)
    else:
        print("Monto no permitido")
else:
    if Usuario != 10334151 and Clave != 1803:
        print("Usuario o clave incorrecto(s)")
        Intento_2 = Intentos - 1
        print("Te quedan", Intento_2)
        Usuario = int(input("Usuario: "))
        Clave = int(input("Clave: "))
        if Usuario != 10334151 and Clave != 1803:
            print("Usuario o clave incorrecto(s)")
            Intento_3 = Intento_2 - 1
            print("Te quedan", Intento_3)
            Usuario = int(input("Usuario: "))
            Clave = int(input("Clave: ")) 
            if Usuario != 10334151 and Clave != 1803:
                print("Usuario o clave incorrecto(s)")
                print("Se han acabado los intentos")
                print("Tarjeta bloqueada")      