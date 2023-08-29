#Cajero Automático
saldo_cajero=1000000
saldo_cuenta=100000
intentos=3
clave_invalida=True
usuario=input("Ingrese usuario: ")
clave=input("Ingrese clave: ")
while clave_invalida and intentos>1:
  if clave=="1803":
    clave_invalida=False
  else:
    clave_invalida=True
    intentos=intentos-1
    clave=input("clave invalida, reingrese clave")
  monto=input("ingrese monto a retirar:")
monto=int(monto)

if monto>=saldo_cuenta:
  print("monto no permitido")
else:
  saldo_cajero=saldo_cajero-monto
  saldo_cuenta=saldo_cuenta-monto
  print("saldo cajero=",saldo_cajero)
  print("saldo cuenta=",saldo_cuenta)
