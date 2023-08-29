#Cajero Automático
saldoCajero = 1000000
saldoenCuenta = 100000
usuario1 = 10334151
clave1 = 1803
intentos = 0

usuario =int(input("ingrese su usuario: "))
while usuario != usuario1:
    usuario = int(input("ingrese su usuario: "))

clave = int(input("ingrese su clave: "))
while clave != clave1:
    clave = int(input("clave invalida, reintente: "))
    intentos = intentos + 1
    if intentos == 3:
        print("Clave bloqueada")
        break

if clave == clave1:
    montoaRetirar = int(input("ingrese monto a retirar: "))
if montoaRetirar >= saldoCajero and montoaRetirar >= saldoenCuenta:
    print("Monto no permitido")
if saldoenCuenta >= montoaRetirar:
    saldoenCuenta =  saldoenCuenta - montoaRetirar
    saldoCajero = saldoCajero - montoaRetirar

print("saldo cuenta=",saldoenCuenta)
print("saldo cajero=",saldoCajero)     