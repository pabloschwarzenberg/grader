#Cajero Automático
saldo_cajero=1000000
saldo_cuenta=100000
intentos=3
clave_invalida=True
usuario=input('ingrese usuario')
clave=input("ingresa clave")
while clave_invalida and intentos>1 :
    if clave=='1803':
        clave_invalida=False
    else:
        clave_invalida=True
        intentos=intentos-1
        clave=input('ingrese clave:')
if clave=='1803':
    
    monto=input("ingrese el monto a retirar: ")
    monto=int(monto)
    saldo_cajero=saldo_cajero-monto
    saldo_cuenta=saldo_cuenta-monto
    x=str(saldo_cajero)
    y=str(saldo_cuenta)
    print('saldo cuenta=',y)
    print('saldo cajero=',x)
    
else:
    print("tarjeta bloqueada")
    