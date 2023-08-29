#Cajero Automático
usuario=input("usuario:")
clave=int(input("clave:"))

if clave==1803:
 monto=int(input("monto:"))
 if monto>100000:
  print("monto no permitido")
 if monto<=100000:
  c=100000-monto
  d=1000000-monto
  print("saldo cuenta=",c)
  print("saldo cajero=",d)
else:
 print("clave invalida")
 clave=int(input("clave:"))
 if clave==1803:
  monto=int(input("monto:"))
  if monto>100000:
   print("monto no permitido")
 if monto<=100000:
  c=100000-monto
  d=1000000-monto
  print("saldo cuenta=",c)
  print("saldo cajero=",d)
 else:
  print("clave invalida")
  clave=int(input("clave:"))
  if clave==1803:
   monto=int(input("monto:"))
   if monto>100000:
    print("monto no permitido")
   if monto<=100000:
    c=100000-monto
    d=1000000-monto
    print("saldo cuenta=",c)
    print("saldo cajero=",d)
  else:
   print("tarjeta bloqueada")
