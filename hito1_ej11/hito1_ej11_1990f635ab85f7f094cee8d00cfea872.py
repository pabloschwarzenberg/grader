#Cajero Automático
Usuario = 10334151
Clave = 1803
Saldo_Cuenta = 100000
Saldo_Cajero = 1000000
Intentos = 3
billetes_20 = 20000
billetes_10 = 10000
billetes_5 = 5000
def billetes_total(c,x):
    billetes = c // x
    resto_billetes = c % x
    return billetes, resto_billetes
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
        b, r = billetes_total(Retiro, billetes_20)
        c, r = billetes_total(r, billetes_10)
        j, r = billetes_total(r, billetes_5)
        print("¡Retiro con exito! Su saldo en nuestro banco es: ")
        print("Saldo Cuenta =", Resta_Cuenta)
        print("Saldo Cajero =", Resta_Cajero)
        print("billetes 20000="+str(b))
        print("billetes 10000="+str(c))
        print("billetes 5000="+str(j))
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