contador=0
intentos=1
while contador<1:
 a=int(input("ingrese numero de usuario: "))
 b=int(input("ingrese contrasena: "))
 saldo_cuenta=100000
 saldo_cajero=1000000
 if a==10334151 and b==1803:
  retiro=int(input("ingrese cantidad a retirar: "))
  if retiro<=100000 or retiro>0:
   contador=contador+1
   saldo_cuenta=saldo_cuenta-retiro
   saldo_cajero=saldo_cajero-retiro
   print("saldo cuenta=",saldo_cuenta)
   print("saldo cajero=",saldo_cajero)
  else:
   print("monto no permitido")   
 elif a!=10334151:
  print("usuario no valido")
  break
 elif a==10334151 and b!=1803:   
  if intentos==3:
   print("tarjeta bloqueada")
   break
  else: 
   intentos=intentos+1
   print("clave invalida")    