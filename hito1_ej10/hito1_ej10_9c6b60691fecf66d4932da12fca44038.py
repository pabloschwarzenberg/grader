usuario=input("usuario:")
clave=int(input("clave:"))

if clave==1803:
 m=int(input("monto:"))
 if m>100000:
  print("monto no permitido")
 if m<=100000:
  c=100000-m
  d=1000000-m
  print("saldo cuenta=",c)
  print("saldo cajero=",d)
else:
 print("clave invalida")
 clave=int(input("clave:"))
 if clave==1803:
  m=int(input("monto:"))
  if m>100000:
   print("monto no permitido")
 if monto<=100000:
  c=100000-m
  d=1000000-m
  print("saldo cuenta=",c)
  print("saldo cajero=",d)
 else:
  print("clave invalida")
  clave=int(input("clave:"))
  if clave==1803:
   m=int(input("monto:"))
   if m>100000:
    print("monto no permitido")
   if monto<=100000:
    c=100000-m
    d=1000000-m
    print("saldo cuenta=",c)
    print("saldo cajero=",d)
  else:
   print("tarjeta bloqueada")