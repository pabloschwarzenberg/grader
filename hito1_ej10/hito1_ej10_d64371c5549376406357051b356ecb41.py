#Cajero Automático
saldo_c=1000000
saldo_u=1000000
salir="N"
while salir=="N":
   i=3
   u=input("ingrese usuario:")
   while i>0:
     c=input("ingrese clave:")
     if u=="10334151" and c=="1803":
         print("usuario y clave correctos")
         break
     elif c!="1803" or u!="10334151":
       i=i-1
       print("usuario o clave incorrectos")
   if i==0:
      print("tarjeta bloqueada")
   else:
      monto_r=int(input("ingrese monto:"))
      if monto_r<saldo_c and monto_r<saldo_u:
           saldo_c=saldo_c-monto_r
           saldo_u=saldo_u-monto_r
           print("saldo de la cuenta=",saldo_u)
           print("saldo del cajero=",saldo_c)
      else:
             print("monto no valido")
    
    

