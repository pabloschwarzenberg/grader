#Cajero Automático
dinerocajero=1000000
dinerotarjeta=100000
a=3
x=int(input("usuario "))
while a!=0:
  y=int(input("clave ")) 
    
  if x==10334151 and y==1803:
     z=int(input("monto a retirar "))
     if z<=dinerotarjeta:
        print("saldo cuenta="+str(dinerotarjeta-z))
        print("saldo cajero="+str(dinerocajero-z))
        break
     else:
        print("monto no permitido")
  else:
      print("clave invalida")
      a=a-1

if a==0:
   print("tarjeta bloqueada")
  