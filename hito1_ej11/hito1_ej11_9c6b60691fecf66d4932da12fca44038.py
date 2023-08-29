#Cajero Automático
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
  q=m%20000
  
  t=q%10000
  v=int((m-(q))/20000)
  z=int((q-(q%10000))/10000)
  s=int((t-(t%5000))/5000)
  print("suma=",m)
  print("billetes 20000=",v)
  print("billetes 10000=",z)
  print("billetes 5000=",s)
else:
 print("clave invalida")
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
  q=m%20000
  t=q%10000
  v=int((m-(q))/20000)
  z=int((q-(q%10000))/10000)
  s=int((t-(t%5000))/5000)
  print("suma=",m)
  print("billetes 20000=",v)
  print("billetes 10000=",z)
  print("billetes 5000=",s)
 else:
  print("clave invalida")
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
    q=m%20000
    t=q%10000
    v=int((m-(q))/20000)
    z=int((q-(q%10000))/10000)
    s=int((t-(t%5000))/5000)
    print("suma=",m)
    print("billetes 20000=",v)
    print("billetes 10000=",z)
    print("billetes 5000=",s)
  else:
   print("tarjeta bloqueada")
      