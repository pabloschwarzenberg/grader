

saldo_cajero=1000000
saldo_cuenta=100000
intentos=3
usuario=input("ingrese usuario: ")
clave_invalida=True
clave=input("ingresa clave: ")
while clave_invalida and intentos>1:
   if usuario=="10334151" and clave=="1803":
     clave_invalida=False
   else:
      clave_invalida=True
      intentos=intentos-1
      clave=input("ingresa clave: ")

if clave=="1803":
   monto=input("ingrese monto a retirar: ")
   monto=int(monto)
   if monto>100000:
    print("monto no permitido")
    monto=input("ingrese monto a retirar: ")
   else:
     saldo_cajero=saldo_cajero-monto
     saldo_cuenta=saldo_cuenta-monto
     print("saldo cuenta =",saldo_cuenta)
     print("saldo cajero=",saldo_cajero)
else:
   print("tarjeta bloqueada")


      