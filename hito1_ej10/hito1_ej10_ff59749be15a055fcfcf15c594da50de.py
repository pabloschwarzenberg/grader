#Cajero Automático
saldoinicialcajero = 1000000
saldoinicialcuenta = 100000
usuario = int(input("Ingrese usuario: "))
while usuario != 10334151:
    usuario = int(input("Ingrese usuario: "))
clave = int(input("Ingrese clave: "))
intentos=0
while (clave!=1803):
    intentos = intentos+1
    if intentos == 3:
        print("Tarjeta bloqueada")
        break
    else:
        clave = int(input("Clave invalida: "))

saldofinalcuenta = 0
saldofinalcajero = 0

if intentos != 3:
    respuesta ="n"
    while (respuesta == "n"):
        monto = int(input("Monto a retirar: "))
        if monto>100000 or monto<0:
            print("Monto no permitido")
        else:
            saldofinalcajero = saldoinicialcajero - monto
            saldofinalcuenta = saldoinicialcuenta - monto
            print("saldo cuenta="+str(saldofinalcuenta))
            print("saldo cajero="+str(saldofinalcajero))
        respuesta = input("Si quiere volver a operar ingrese (n), si no, ingrese cualquier otra letra: ")