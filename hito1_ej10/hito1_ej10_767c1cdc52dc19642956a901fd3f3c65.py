#Cajero Automático
saldo_cajero=1000000
usuario=input("usuario: ")
intentos=2
clave_invalida=True
clave=input("ingresa clave: ")
while clave_invalida and intentos>0:
   if clave=="1803":
    clave_invalida=False
   else:
    clave_invalida=True
    print("clave invalida")
    intentos=intentos-1
    clave=input("ingresa clave: ")

if clave=="1803":
  monto=input("ingrese monto a retirar: ")
  monto=int(monto)
  monto_invalido=True
  while monto_invalido:
     if monto<=100000 and monto>=0:
        monto_invalido=False
     else:
        monto_invalido=True
        print("monto no permitido")
  saldo_cuenta=100000-monto     
  saldo_cajero=saldo_cajero-monto
  print("saldo cuenta=",saldo_cuenta)
  print("saldo cajero=",saldo_cajero)
else:
  print("tarjeta bloqueada")
