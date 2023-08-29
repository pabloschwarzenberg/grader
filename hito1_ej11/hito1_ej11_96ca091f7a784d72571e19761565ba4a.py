import sys
cajero=1000000
usuario=10334151
clave=1803
saldo=100000
billetes20=20
billetes10=40
billetes5=40
billetes20t=0
billetes10t=0
billetes5t=0
usuarioing=int(input("ingrese usuario"))
claveing=int(input("ingrese clave"))
x=0
while claveing!=clave:
  x+=1
  if x==3:
    print("tarjeta bloqueada")
    sys.exit()
  claveing=int(input("error, ingrese clave"))
if claveing==clave:
  giro=int(input("ingrese monto a retirar"))
if giro<saldo and giro<cajero:
  cajero-=giro
  saldo-=giro
print("saldo cuenta=",saldo)
print("saldo cajero=",cajero)
while giro>0:
  if giro>=20000:
    billetes20t+=1
    giro-=20000
  elif giro>=10000:
    billetes10t+=1
    giro-=10000
  elif giro>=5000:
    giro-=5000
print("billetes 20000=",billetes20t)
print("billetes 10000=",billetes10t)
print("billetes 5000=",billetes5t)