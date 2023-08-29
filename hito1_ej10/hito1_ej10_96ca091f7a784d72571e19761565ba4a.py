import sys
cajero=1000000
usuario=10334151
clave=1803
saldo=100000
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