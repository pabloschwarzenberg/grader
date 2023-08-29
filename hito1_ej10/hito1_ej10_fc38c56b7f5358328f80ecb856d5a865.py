#Cajero Automático
usuario=int(input("ingrese numero de usuario: "))
clave=int(input("ingrese su clave: "))


if usuario == 10334151:
    if clave !=1803:
        intento=1
        while intento < 3:
            print("clave invalida")
            if intento==3:
                print("tarjeta bloqueada")
                break

    else:
        saldoI = 1000000
        cuenta=100000
        monto=int(input("ingrese monto a retirar: "))
        if monto > cuenta:
            print("monto no permitido")
        else:
            ns=cuenta-monto
            nc=saldoI-monto
            print("saldo cuenta="+str(ns)+","+"saldo cajero="+str(nc))