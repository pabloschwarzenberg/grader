#Cajero Automático
saldo_cajero=1000000
saldo_usuario=100000
usuario_invalida=True
usuario=input("ingresa usuario:") 
while usuario_invalida:
    if usuario=="10334151":
        usuario_invalida=False
    else:
        usuario_invalida=True
        usuario=input("ingresa usuario:")
if usuario=="10334151":
    clave=input("digite clave:")
    intentos=3
    clave_invalida=True
    while clave_invalida and intentos>1:
        if clave=="1803":
            clave_invalida=False
        else:
            clave_invalida=True
            intentos=intentos-1
            clave=input("ingrese usuario:")
    monto=input("ingrese monto a retirar:")
    monto=int(monto)
    saldo_usuario=True
    while saldo_usuario:
        if monto<=100000:
            saldo_usuario=False
        else:
            saldo_usuario=True
            print("ingrese un monto disponible:")
else:
    intentos=intentos-1
    print("tarjeta bloqueada")
monto=int(monto)
saldo_usuario=100000
saldo_cajero=saldo_cajero-monto
saldo_usuario=saldo_usuario-monto    
print("saldo cuenta=",saldo_usuario) 
print("saldo cajero=",saldo_cajero)
