saldo_cajero=1000000
saldo_cuenta=100000
intentos=3
clave_invalida=True
usuario_invalido=True

usuario=input("ingrese numero de usuario:")
clave=input("ingrese clave:")

while ((clave_invalida)and(usuario_invalido))and intentos>1:
  if ((clave =="1803")and(usuario=="10334151")):
    clave_invalida=False
    usuario_invalido=False
  if((clave!="1803")and(usuario=="10334151")):
    clave_invalida=True
    intentos=intentos-1
    clave=input("ingrese clave:")
  if((clave=="1803")and(usuario!="10334151")):
    usuario_invalido=True
    print("usuario invalido")
    usuario=input("ingrese numero de usuario:")
    
  
     
  
if ((clave=="1803")and(usuario=="10334151")):
  monto=int(input("ingresa monto a retirar:"))
  if (monto<100000):
      saldo_nuevo_cajero=saldo_cajero-monto
      saldo_nuevo_cuenta=saldo_cuenta-monto
      print("Saldo cuenta=",saldo_nuevo_cuenta)
      print("Saldo cajero=",saldo_nuevo_cajero)
  elif(monto>100000):
      print("Saldo insuficiente")
  
else:
  print("tarjeta bloqueada")
    