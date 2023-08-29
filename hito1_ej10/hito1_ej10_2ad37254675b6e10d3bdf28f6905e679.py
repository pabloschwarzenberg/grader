saldo_cajero=1000000
saldo_usuario=100000
intentos=3
clave_invalida=True
usuario=input("ingrese usuario")
clave=input("ingrese clave")
while clave_invalida and intentos>1:
 if clave=="1803":
    clave_invalida=False
 else:
        clave_invalida=True
        intentos=intentos-1
        clave=input("reingrese clave:")

        
 monto=input("ingrese monto a retirar")
monto=int(monto)
if monto >= saldo_usuario:
 print("monto no permitido")
else:
    saldo_cajero=saldo_cajero-monto
    saldo_usuario=saldo_usuario-monto
    print("saldo cajero=",saldo_cajero)
    print("saldo cuenta=",saldo_usuario)