#Cajero Automático
monto_i=1000000
monto_p=100000
i=0
while i<3:
    usuario=int(input("Ingrese usuario: "))
    clave=int(input("Igrese clave: "))
    if clave==1803 and usuario==10334151:
        monto_r=int(input("Monto a retirar: "))
        break
    else:
        print("clave invalida")
    i=i+1
if monto_r <= monto_p:
    saldo_cuenta= monto_p - monto_r
    print("saldo cuenta=",saldo_cuenta)
    saldo_cajero= monto_i - monto_r
    print("saldo cajero=",saldo_cajero)
else:
    print("monto no permitido")
    