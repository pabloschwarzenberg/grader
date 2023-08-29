saldo_cajero=1000000
saldo_cliente=100000
intentos=4
clave_invalida=True
usuario= int(input("ingrese usurio"))
if usuario==10334151:
    while clave_invalida and intentos>1:
        clave= int(input("clave"))
        if clave==1803:
            clave_invalida=False
        else:
            clave_invalida=True
            intentos=intentos-1
    if clave==1803:
        monto=int(input("Ingrese mont a retirar: "))
        if  0<monto<saldo_cliente:
            saldo_cajero=saldo_cajero-monto
            saldo_cliente=saldo_cliente-monto
            print("saldo cuenta="+str(saldo_cliente)+"")
            print("saldo cajero="+str(saldo_cajero)+"")
        else:
            print("monto no valido")
    else:
        print("Tarjeta bloqueada")