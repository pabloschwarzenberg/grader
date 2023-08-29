#Cajero Automático
dinero_inicial = int(1000000)
cuenta = int(100000)

rut = 10334151
clave = 1803
r=int(input("ingrese rut: "))#1
c=int(input("ingrese clave: "))

if r == rut and c == clave:
    retiro=int(input("¿cuanto dinero desea retirar?: "))
    if retiro >= dinero_inicial:
        print("monto no permitido")
    if retiro <= dinero_inicial:
        total_cuenta = cuenta - retiro
        print("saldo cuenta = ",total_cuenta)
        total_cajero = dinero_inicial - retiro
        print("saldo cajero =",total_cajero)



while r != rut or c != clave:
    if r != rut or c != clave:
        print("clave invalida")
        r = int(input("ingrese rut: "))#2
        c = int(input("ingrese clave: "))
        if r != rut or c != clave:
            print("clave invalida")
            r = int(input("ingrese rut: "))  # 3
            c = int(input("ingrese clave: "))
            if r != rut or c != clave:
                print("tarjeta bloqueada")
    break