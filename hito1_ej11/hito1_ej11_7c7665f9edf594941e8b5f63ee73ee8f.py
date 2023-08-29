user = 10334151
clave = 1803
saldo = 100000
lucas20 = 20
lucas10 = 40
lucas5 = 40
saldocajero = 1000000
userinp = int(input("Ingresar usuario: "))
claveinp = int(input("Ingresar clave: "))
correcto = 0
while correcto != 5:
    if claveinp != clave:
        print("Clave inválida")
        claveinp = int(input("Ingresar clave: "))
        correcto = correcto+1
    if correcto == 2:
        print("Tarjeta bloqueada")
        quit()
    if claveinp == clave:
        correcto = 5
if claveinp == clave:
    correcto = 5
    monto = int(input("Ingrese el monto a retirar"))
    if monto not in range(1, saldo) or monto not in range(1, saldocajero):
        print("monto no permitido")
    else:
        saldo = saldo-monto
        saldocajero = saldocajero-monto
        print("saldo cuenta=", saldo)
        print("saldo cajero=", saldocajero)
        lucas20 = monto/20000
        monto = monto%20000
        lucas10 = monto/10000
        monto = monto%10000
        lucas5 = monto/5000
        monto = monto%5000
        print("Billetes 20000=", round(lucas20))
        print("Billetes 10000=", round(lucas10))
        print("Billetes 5000=", round(lucas5))

