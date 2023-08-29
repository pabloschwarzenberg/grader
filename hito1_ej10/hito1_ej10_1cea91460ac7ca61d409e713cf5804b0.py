#Cajero Automático
import sys
iliketrains=0
cajero=1000000
saldo=100000
intentos=0
while iliketrains==0:
  x=int(input())
  y=int(input())
  if x==10334151 and y==1803:
    monto=int(input())
    if monto<=0 or monto>100000:
      print("monto no permitido")
    else:
      cajero-=monto
      saldo-=monto
      print("saldo cuenta="+str(saldo))
      print("saldo cajero="+str(cajero))
      l=input()
      if l!="N":
        break
  
  elif intentos<3:
      print("clave invalida")
      intentos+=1
  else:
      print("tarjeta bloqueada")
      sys.exit(0)