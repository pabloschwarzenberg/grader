#Cajero Automático
x=0
N=-20
dinero=100000
plata_cajero=1000000
while x<3:
 usuario=int(input("Ingrese su nro de usuario"))
 clave=int(input("Ingrese su contraseña"))
 x=x+1
 if (usuario!=10334151) and (clave!=1803)and x==3:
   print("Tarjeta bloqueada")
   break
 elif (usuario==10334151) and (clave==1803):
  sacar=int(input("Cuanto dinero desea retirar:"))
  dinero=dinero-sacar
  plata_cajero=plata_cajero-sacar
  break
an=20
bn=40
cn=40
a=0
b=0
c=0
if int(sacar/20000)>=1 and an<=20:
  a=int(sacar/20000)
  sacar=sacar-20000*a
if int(sacar/10000)>=1 and bn<=40:
  b=int(sacar/10000)
  sacar=sacar-10000*b
if int(sacar/5000)>=1 and cn<=40:
  c=int(sacar/5000)
  sacar=sacar-5000*c
print("billetes 20000=",a)
print("billetes 10000=",b)
print("billetes 5000=",c)
print("saldo cuenta=",dinero)
print("Saldo cajero=",plata_cajero)   