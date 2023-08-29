#Cajero Automático
contador=0
saldoCa=1000000
saldoCu=100000
clave=0
Usuario=0
Bloqueo=False
while clave!="1803" and Usuario!="10334151":
 if contador==3:
   Bloqueo=True
   break
 Usuario=input("ingrese usuario: ")
 clave=input("ingrese clave: ")
 if clave!="1803" and Usuario!="10334151":
   contador=contador+1
   print("clave invalida")
if Bloqueo==True:
  print("tarjeta bloqueada")
while clave=="1803" and Usuario=="10334151" and Bloqueo==False:
  retractar=int(input("ingrese cuanto desea retirar: "))
  saldoCu=saldoCu-retractar
  saldoCa=saldoCa-retractar
  print("saldo cuenta=",saldoCu)
  print("saldo cajero=", saldoCa)
  break