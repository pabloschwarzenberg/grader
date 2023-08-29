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
print("saldo cuenta=",dinero)
print("Saldo cajero=",plata_cajero)     