#Cajero Automático
usuario=int(input())
x="N"
while x=="N":
  a=2
  clave=1803
  y=int(input("ingrese clave",))
  q=6
  while clave!=y:
      if a>0:
          a-=1
          print("clave invalida")
          y=int(input("reingrese clave",))
      else:
          q=5
          break
  if q==5:
    print("tarjeta bloqueada")
    break 
  else:
    print("clave correcta")
    monto=int(input())
    if monto>100000:
      print("monto no permitido")
    else:
      print("saldo cuenta=",100000-monto)
      print("saldo cajero=",1000000-monto)
    x=str()      
        

