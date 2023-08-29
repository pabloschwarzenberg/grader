contador=0
intentos=1
cantidad_de_20=20
cantidad_de_10=40
cantidad_de_5=40
billetes_de_20=0
billetes_de_10=0
billetes_de_5=0
while contador<1:
 a=int(input("ingrese numero de usuario: "))
 b=int(input("ingrese contrasena: "))
 saldo_cuenta=100000
 saldo_cajero=1000000
 if a==10334151 and b==1803:
  retiro=int(input("ingrese cantidad a retirar: "))
  retiro1=retiro
  if retiro<=100000 and retiro>0 and retiro%5000==0:  
   while retiro1>0:
    if retiro1>=20000 and cantidad_de_20!=0:
     retiro1=retiro1-20000
     billetes_de_20=billetes_de_20+1
     cantidad_de_20=cantidad_de_20-1
    elif 10000<=retiro1<20000 and cantidad_de_10!=0 or cantidad_de_20==0 and retiro1>=10000 and cantidad_de_10!=0:
     retiro1=retiro1-10000
     billetes_de_10=billetes_de_10+1
     cantidad_de_10=cantidad_de_10-1
    elif retiro1<10000 or cantidad_de_20==0 and retiro1<10000 or cantidad_de_20==0 and cantidad_de_10==0:
     retiro1=retiro1-5000
     billetes_de_5=billetes_de_5+1
     cantidad_de_5=cantidad_de_5-1   
   contador=contador+1
   saldo_cuenta=saldo_cuenta-retiro
   saldo_cajero=saldo_cajero-retiro
   print("saldo cuenta=",saldo_cuenta)
   print("saldo cajero=",saldo_cajero)
   print("billetes 20000=",billetes_de_20)
   print("billetes 10000=",billetes_de_10)
   print("billetes 5000=",billetes_de_5)
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