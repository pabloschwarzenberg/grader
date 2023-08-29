saldoic = 1000000
saldocajero = 100000

clave = str(input("Ingrese clave: "))
usuario = str(input("Ingrese usuario: "))

#contador
c = 0

if clave != "1803":

    print("Clave invalida, ingrese otra vez")

    while clave != "1803" and c < 3:
        c = c + 1
        clave = str(input("Ingrese Clave: "))  ##aqui da el error :C

    print("Tarjeta Bloqueada")

else:
    mr = 45000

    if mr > 100000:
        print("Monto no permitido")

        print("saldo cuenta=", saldoic)
        print("saldo cajero=", saldocajero)

    else:
        saldofc = saldoic - mr
        saldocajerof = saldocajero - mr

        print("saldo cuenta= ", saldofc)
        print("saldo cajero= ", saldocajerof)