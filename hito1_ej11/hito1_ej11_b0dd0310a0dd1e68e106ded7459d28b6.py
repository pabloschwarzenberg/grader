#Cajero Automático
import sys
saldo_inicial = 1000000
billete20 = [20, 20000]
billete10 = [40, 10000]
billete5 = [40, 5000]
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
            if monto_retiro == 5000:
                print("billetes 5000 = 1")
            if monto_retiro == 10000:
                print("Billetes 10000 = 1")
            if monto_retiro == 15000:
                print("Billetes 10000 = 1")
                print("Billetes 5000 = 1")
            if monto_retiro == 20000:
                print("Billetes 20000 = 1")
            if monto_retiro == 25000:
                print("Billetes 20000 = 1")
                print("Billetes 5000 = 1")
            if monto_retiro == 30000:
                print("Billetes 20000 = 1")
                print("Billetes 10000 = 1")
            if monto_retiro == 35000:
                print("Billetes 20000 = 1")
                print("Billetes 10000 = 1")
                print("Billetes 5000 = 1")
            if monto_retiro == 40000:
                print("Billetes 20000 = 2")
            if monto_retiro == 45000:
                print("Billetes 20000 = 2")
                print("Billetes 5000 = 1")
            if monto_retiro == 50000:
                print("Billetes 20000 = 2")
                print("Billetes 10000 = 1")
            if monto_retiro == 55000:
                print("Billetes 20000 = 2")
                print("Billetes 10000=1")
                print("Billetes 5000=1")
            if monto_retiro == 60000:
                print("Billetes 20000 = 3")
            if monto_retiro == 65000:
                print("Billetes 20000 = 3")
                print("Billetes 5000=1")
            if monto_retiro == 70000:
                print("Billetes 20000 = 3")
                print("Billetes 10000 = 1")
            if monto_retiro == 75000:
                print("Billetes 20000 = 3")
                print("Billetes 10000 = 1")
                print("Billetes 5000=1")
            if monto_retiro == 80000:
                print("Billetes 20000 = 4")
            if monto_retiro == 85000:
                print("Billetes 20000 = 4")
                print("Billetes 5000=1")
            if monto_retiro == 90000:
                print("Billetes 20000 = 4")
                print("Billetes 10000 = 1")
            if monto_retiro == 95000:
                print("Billetes 20000 = 4")
                print("Billetes 10000 = 1")
                print("Billetes 5000=1")
            if monto_retiro == 100000:
                print("Billetes 20000 = 5")
            print ("Saldo cuenta=",saldo_cuenta - monto_retiro)
            print ("saldo cajero=",saldo_inicial - monto_retiro)
            
    