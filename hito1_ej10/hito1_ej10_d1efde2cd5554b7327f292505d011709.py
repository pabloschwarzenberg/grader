usuario=int(input("ingrese numero de usuario: "))
usuario_correcto=False
saldo_cajero=1000000
saldo_cuenta=100000
intentos=3
clave_invalida=True
while usuario_correcto==False:
    if usuario==10334151:
        usuario_correcto=True
    else:
        print("usuario incorrecto")
        usuario=input("ingrese numero de usuario nuevamente: ")

clave=input("ingresa clave: ")
while clave_invalida==True and intentos>1:
    if clave=="1803":
        clave_invalida=False
    else:
        Clave_invalida=True
        intentos=intentos-1
        print("clave invalida")
        clave=input("ingrese clave: ")
if clave=="1803":
    print("clave correcta")
    monto=input("ingrese monto a retirar: ")
    monto=int(monto)
    saldo_cajero=saldo_cajero-monto
    saldo_cuenta=saldo_cuenta-monto
    if saldo_cuenta<0:
        print("monto no permitido")
    else:
        print("saldo cuenta=" + str(saldo_cuenta))
        print("saldo cajero=" + str(saldo_cajero))
else:
    print("tarjeta bloqueada")