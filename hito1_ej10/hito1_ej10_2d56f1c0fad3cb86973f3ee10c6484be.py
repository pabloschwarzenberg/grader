#Cajero Automático
intentos=3
saldo_inicial=1000000
saldo_usuario=100000
clave_invalida=True
usuario=input("ingrese numero de usuario:")
clave=input("ingrese clave:")
while clave_invalida and 1<intentos:
  if clave=="1803":
    clave_invalida=False
  else:
      clave_invalida=True
      intentos=intentos-1
      clave=input("clave invalida, reingrese clave")
  monto=input("ingrese monto a retirar:")
monto=int(monto)
if saldo_usuario<=monto:
   print("monto no permitido")
else:
  saldo_cajero=1000000-monto
  saldo_usuario=100000-monto
  print("saldo cajero=",saldo_cajero)
  print("saldo cuenta=",saldo_usuario)
    