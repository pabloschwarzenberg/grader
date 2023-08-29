#Cajero Automático
saldo_cajero=1000000
saldo_usuario=100000
intentos=3
clave_invalida=True
usuario=int(input("ingrese usuario: "))
clave=input("ingrese clave: ")
while clave_invalida and intentos>1:
 if clave=="1803":
    clave_invalida=False
 else:
    clave_invalida=True
    intentos=intentos-1
    print("clave invalida")
    clave=input("ingrese clave: ")
if usuario==10334151:
 if clave=="1803":
  monto=int(input("ingrese monto a retirar: "))
  if monto<100000:
   saldo_cajero=saldo_cajero-monto
   saldo_usuario=saldo_usuario-monto
   print("saldo cuenta=",saldo_usuario)
   print("saldo cajero=",saldo_cajero)
  else:
    print("monto no permitido")
else:
 print("tarjeta bloqueada")


