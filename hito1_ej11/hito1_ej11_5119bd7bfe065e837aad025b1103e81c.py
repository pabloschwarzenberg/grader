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
  q=monto%20000
  
  t=q%10000
  v=int((monto-(q))/20000)
  z=int((q-(q%10000))/10000)
  s=int((t-(t%5000))/5000)
  print("suma=",monto)
  print("billetes 20000=",v)
  print("billetes 10000=",z)
  print("billetes 5000=",s)
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
  q=monto%20000
  t=q%10000
  v=int((monto-(q))/20000)
  z=int((q-(q%10000))/10000)
  s=int((t-(t%5000))/5000)
  print("suma=",monto)
  print("billetes 20000=",v)
  print("billetes 10000=",z)
  print("billetes 5000=",s)
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
    q=monto%20000
    t=q%10000
    v=int((monto-(q))/20000)
    z=int((q-(q%10000))/10000)
    s=int((t-(t%5000))/5000)
    print("suma=",monto)
    print("billetes 20000=",v)
    print("billetes 10000=",z)
    print("billetes 5000=",s)
  else:
   print("tarjeta bloqueada")

