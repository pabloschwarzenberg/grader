sc=1000000 
su=100000 
r=0
n = 0
while n < 3:
  u=str(input("Ingrese Nº de Usuario:""Ingrese clave:"))
  c=str(input(""))

  if u==str(10334151) and c==str(1803):
    r=int(input("Monto a retirar:"))
    if r>su:
      print ("Monto no permitido")
    elif r<=su:
      sc=sc-r
      su=su-r
      print("saldo cuenta=",su)
      print("saldo cajero=",sc) 
        
  else :
    print("clave y/o contraseña invalida")
    n = n+1
    
if n==2:
   print("")
else:
  print("Tarjeta bloqueada")

      print("saldo cajero=",sc) 
        
  else :
    print("clave y/o contraseña invalida")
    n = n+1
    
if n==2:
   print("")
else:
  print("Tarjeta bloqueada")
