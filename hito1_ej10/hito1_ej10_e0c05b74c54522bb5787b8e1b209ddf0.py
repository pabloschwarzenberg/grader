saldo_cajero=1000000
saldo_cuenta=100000
a=3
while a>0:
  b=int(input("usuario"))
  c=int(input("clave"))
  if b!=10334151 or c!=1803:
    print("clave invalida")
    a=a-1
  elif b==10334151 and c==1803:
    while True:
      d=int(input("dinero"))
      if d<=saldo_cajero and d<=saldo_cuenta:
        print("saldo cuenta=",saldo_cuenta-d)
        print("saldo cajero=",saldo_cajero-d)
        break
      else:
        print("monto no permitido")
        break
    break
if a==0:
  print("tarjeta bloqueada")
     
        
  