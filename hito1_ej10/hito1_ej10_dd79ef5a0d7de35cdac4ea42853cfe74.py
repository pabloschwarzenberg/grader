
cajero=1000000
cuenta=100000
usuario=10334151
clave=1803
cont=0
while cont<3:
    cl=int(input("Ingrese clave: "))
    if cl==clave:
        monto_a_retirar=int(input("Ingrese monto a retirar: "))
        break
    else:
        cont=cont+1
        print("ERROR! Contraseña invalida")
        if cont==3:
            print("Tarjeta bloqueada")
            break

if monto_a_retirar<=cuenta:
    saldocuenta=cuenta-monto_a_retirar
    saldocajero=cajero-monto_a_retirar
    print("saldo cuenta=",saldocuenta)
    print("saldo cajero=",saldocajero)
else:
    print("Monto no permitido")