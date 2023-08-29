usuario=input("Ingrese Usuario: ")
saldo_cuenta_corriente=100000
saldo_cajero=1000000
monto_retiro=int()
saldo_restante=(saldo_cuenta_corriente)-(monto_retiro)
i = 0
while i<3:
    clave=float(input("Ingrese clave: "))
    if clave!=1803 and i<2:
        print("clave invalida")
    elif clave!=1803 and i<3:
        print("clave bloqueada")
    elif clave==1803:
        monto_retiro = int(input("Ingrese monto a retirar: "))
        if monto_retiro>saldo_restante:
            print("Monto Invalido")
        if  monto_retiro<saldo_restante:
            print("saldo cuenta=",(saldo_restante)-(monto_retiro))
            print("saldo cajero=",(saldo_cajero)-(monto_retiro))
            N = monto_retiro
            denominaciones = [20000, 10000, 5000]

            for denominacion in denominaciones:
                print("Billetes", denominacion, "=%d" % (N / denominacion))
                N = N % denominacion

            break
    i += 1