#Cajero Automático
from os import system
system("cls")

saldo_inicial = 1000000
saldo_usuario = 100000
intentos = 0
usuario_valido = 10334151
clave_valida = 1803

while intentos < 3:
    usuario = int(input("Ingrese su usuario: "))
    clave = int(input("Ingrese su clave: "))

    if usuario == usuario_valido and clave == clave_valida:
        monto = int(input("Ingrese el monto a retirar: "))
        if monto <= saldo_usuario:
            saldo_usuario -= monto
            saldo_inicial -= monto
            print("Saldo cuenta={}, Saldo cajero={}".format(saldo_usuario,saldo_inicial,))
        else:
            print("Monto no permitido. Fondos insuficientes.")
        break
    else:
        print("Clave inválida.")
        intentos += 1

if intentos == 3:
    print("Tarjeta bloqueada.")      