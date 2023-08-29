#Cajero Automático Nivel 2
saldocajero = 1000000
billetes20= 20
billetes10= 40
billetes5= 40
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
            while monto != 0:
                if monto%20000 == 0:
                    r = monto//20000
                    billetes20 = billetes20 - r
                    print("billetes 20000=",r)
                    monto = monto - r*20000
                elif monto%10000 == 0:
                    s= monto//10000
                    billetes10 = billetes10 - s
                    print("billetes 10000=",s)
                    monto = monto - s*10000
                elif monto%5000 == 0:
                    t = monto//5000
                    billetes5 = billetes5 - t
                    print("billetes 5000=",t)
                    monto = monto - t*5000
        opcion = input("Presione N para continuar")
        if opcion != "N":
            break
        else:
            continue