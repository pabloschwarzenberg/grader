#Cajero Automático
import sys
saldo_inicial = 1000000
saldo_cuenta = 100000
usuario = int(input("Ingrese número de usuario: "))
while not usuario == 10334151:
    print("ingrese otro número por favor")
    usuario = int(input("Ingrese número de usuario: "))
if usuario == 10334151:
    clave = int(input("ingrese clave de usuario: "))
    a = 0
    while not clave == 1803:
        a = a + 1
        print("No es la clave que corresponde. Inténtelo de nuevo.")
        clave = int(input("ingrese clave de usuario: "))
        if a == 4:
            print("Tarjeta bloqueada")
            sys.exit()
    if clave == 1803:
        monto_retiro = int(input("¿Cuál es el monto a retirar?: "))
        while monto_retiro > 100000:
            print("Monto no permitido.")
            monto_retiro = int(input("¿Cuál es el monto a retirar?: "))
        if monto_retiro <= 100000:
            print ("Saldo cuenta=",saldo_cuenta - monto_retiro)
            print ("saldo cajero=",saldo_inicial - monto_retiro) 