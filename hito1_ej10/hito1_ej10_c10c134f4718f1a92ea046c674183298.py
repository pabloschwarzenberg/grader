#Cajero Automático
#ingresar los datos
U = int(input("ingrese su usuario:"))
C = int(input("ingrese su clave:"))

Usuario = 10334151
Clave = 1803
Intentos = 1
SaldoCajero = 1000000
SaldoCuenta = 100000
#Procesos
while C != Clave :
    Intentos +=1

    if C == Clave:
        print("clave incorrecta")
        break

    if Intentos >3:
        break
    C = int(input("ingrese su clave nuevamente"))
    print("clave invalida")
if Intentos > 3:
    print("tarjeta bloqueada")
if U == Usuario:
    if C == Clave:
        monto = int(input("¿cuanto quiere retirar?"))
        if monto >SaldoCuenta and monto > SaldoCajero:
            print("monto no permitido")
        else:
            SaldoCuenta -= monto
            SaldoCajero -= monto
            print("saldo cuenta=",SaldoCuenta,"")
            print("saldo cajero=",SaldoCajero,"")