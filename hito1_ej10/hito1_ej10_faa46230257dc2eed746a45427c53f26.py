#Cajero Automático
saldo = 1000000
usuario = 10334151
clave = 1803
saldoCuenta = 100000

ingreso = int(input("Ingrese el numero de usuario: "))
while ingreso != usuario:
    ingreso = int(input("Ingrese usuario nuevamente: "))

contra = int(input("Ingrese la clave del usuario: "))
intentos = 0
while contra != clave:
    intentos += 1
    contra = int(input("Clave invalida: "))
    if intentos == 3:
        print("Tarjeta bloqueada")
        break
if intentos != 3:
    retiro = int(input("Ingrese monto a retirar: "))
    if retiro > saldo or retiro >= saldoCuenta:
        print("Monto no permitido")
    else:
        saldo = saldo - retiro
        saldoCuenta = saldoCuenta - retiro
        print("saldo cuenta=",saldoCuenta)
        print("saldo cajero=",saldo)      