#Cajero Automático
 usuario=int(input("usuario"))
 n=0
 if usuario==10334151:
  while n<4:
   clave=int(input("clave"))
   if clave==1803:
     monto=int(input("monto a retirar"))
     if monto<100000:
       print("monto no permitido")
     else:
       cuenta=100000-monto
       cajero=1000000-monto
       print("'saldo cuenta='+str(cuenta)+","'saldo cajero='+str(cajero)")
   #hacer la otra wea
   else:
     n=n+1
  print("tarjeta bloqueada")
   
  