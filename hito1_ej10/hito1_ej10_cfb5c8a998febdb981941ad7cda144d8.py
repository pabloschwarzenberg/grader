#Cajero Automático Nivel 1
saldocajero = 1000000
usuario = input("Ingrese usuario:")
i = 0
while i<3:
    clave = input("Ingrese su clave:")
    if clave == "1803":
        break
    i = i + 1
if clave != "1803":
    print("tarjeta bloqueada")
else:
    saldocuenta= 100000
    while True:
        monto = int(input("¿Cuál es su monto a retirar?"))
        if monto>saldocajero or monto>saldocuenta:
            print("monto no permitido")
            continue
        else:
            saldocajero = saldocajero-monto
            saldocuenta = saldocuenta-monto
            print("saldo cuenta=",saldocuenta)
            print("saldo cajero=",saldocajero)
        opcion = input("Presione N para continuar")
        if opcion != "N":
            break
        else:
            continue