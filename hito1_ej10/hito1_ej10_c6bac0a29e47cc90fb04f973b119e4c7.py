#Cajero Automático
import math
saldo_cajero= 1000000 # un millon
saldo_usuario= 100000 # cien mil
clave = 1803
intento = 3
acceso = 0
usuario = int(input("Ingrese usuario"))
while intento > 0:
    intentclave = int(input("ingrese su clave: "))
    if intentclave != clave:
        intento = intento-1
    if intentclave == clave:
        acceso = 1
        break
        
while acceso == 1:
    montoretir = int(input("Ingrese monto a retirar: "))
    if montoretir > saldo_usuario:
            print("Ingrese un monto valido: ")
    if montoretir < saldo_usuario:
        saldo_usuario = saldo_usuario - montoretir
        saldo_cajero = saldo_cajero - montoretir
        break
        
print("Saldo cuenta=",saldo_usuario)
print("Saldo cajero=",saldo_cajero)


if intento == 0:
    print("tarjeta bloqueada")