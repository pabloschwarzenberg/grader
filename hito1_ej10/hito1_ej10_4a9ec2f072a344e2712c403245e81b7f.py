usuario = 10334151
passw = 1803
saldoUsuario = 100000
saldoCajero = 1000000
cont = 0
conectado = bool
us = int(input("ingrese usuario: "))
while not us == usuario:
    us = int(input("Ingrese nuevamente su usuario: "))
co = int(input("ingrese clave: "))
intentos = 1
while  co !=passw and intentos<3:
    intentos = intentos+1
    co = int(input("Clave invalida, Ingrese nuevamente su clave: "))

if intentos ==3:
        print("Clave bloqueada")
else:
    montoRetiro = int(input("Ingrese monto a retirar: "))
    if montoRetiro>= saldoCajero or montoRetiro>= saldoUsuario:
        print("Monto no permitido")
    else:
        saldoUsuario = saldoUsuario - montoRetiro
        saldoCajero = saldoCajero - montoRetiro
        print("saldo cuenta=", saldoUsuario)
        print("saldo cajero=", saldoCajero)