saldo_cajero=1000000
saldo_usuario=100000
usuario=input("ingrese usuario: ")
usuario_invalido=True
while usuario_invalido:
    if usuario=="10334151":
        usuario_invalido=False
    else:
        print("usuario invalido")
        usuario=input("ingrese usuario: ")
if usuario=="10334151":
    clave_invalida=True
    clave=input("ingrese clave: ")
    intentos=3

    while clave_invalida and intentos>1:
       if clave=="1803":
           clave_invalida=False
       else:
           print("clave invalida")
           clave=input("ingrese clave: ")
           intentos=intentos-1
    

          

if clave=="1803":
    monto=input("ingrese monto a retirar: ")
    monto=int(monto)
    monto_invalido=True
    while monto_invalido:
        if monto>saldo_cajero or monto>saldo_usuario:
           print("monto no permitido")
           monto=input("ingrese monto retirar :")
           monto=int(monto)
        else:
            monto_invalido=False
            saldo_cajero=saldo_cajero-monto
            saldo_usuario=saldo_usuario-monto
            print("saldo cajero=",saldo_cajero)
            print("saldo cuenta=",saldo_usuario)
if intentos==1:
    print("tarjeta bloqueada: ")

      