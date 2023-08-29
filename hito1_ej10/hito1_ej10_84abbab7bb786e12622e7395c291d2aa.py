saldo_usuario=100000
saldo_cajero=1000000
n=3
puede=True
if n==0:
    print('tarjeta bloqueada')
    puede=False
usuario=input('Ingrese el numero de usuario')
clave=input('Ingrese la clave')
if usuario==10334151 and clave==1803 and puede:
    monto=input('Ingrese el monto a retirar')
    if monto>saldo:
        print('monto no permitido')
    else:
        saldo_usuario=saldo_cajero-monto
        saldo_cajero=saldo_cajero-monto
        print('saldo cuenta',saldo_usuario)
        print('saldo cajero',saldo_cajero)
else:
    print("clave invalida")
    n=n-1
