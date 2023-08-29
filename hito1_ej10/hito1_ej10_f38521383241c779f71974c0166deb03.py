#Cajero Automático
saldo_inicial_cajero = 1000000
saldo_inicial = 100000
usuario = int(input("Ingrese Usuario:"))
clave = int(input("Ingrese la clave:"))
intentos = 2

while intentos != 0:
    if clave != 1803:
        print("clave invalida")
        intentos = intentos-1
        clave = int(input("Ingrese la clave:"))
    else:
        monto = int(input("Ingrese el monto a retirar de su cuenta:"))
        if monto < saldo_inicial:
            saldo = saldo_inicial-monto
            saldo_inicial_cajero = saldo_inicial_cajero-monto
            print("saldo cuenta =", saldo)
            print("saldo cajero =", saldo_inicial_cajero)
            break
        else:
            print("monto no permitido")
if intentos == 0:
    print("tarjeta bloqueada")