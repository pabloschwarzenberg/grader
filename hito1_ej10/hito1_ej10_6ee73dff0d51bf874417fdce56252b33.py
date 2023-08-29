#Cajero Automático
saldo=100000
saldocajero=1000000

usuario=input("Usuario: ")
intentos=0
clave=1
while(clave!=1803):
  while(intentos!=3):
   clave=int(input("Clave: "))
   if(clave==1803): 
      break
     
   else:
      print("Clave inválida")
      intentos=intentos+1
  
  else:
      print("tarjeta bloqueada")
      break

retiro=int(input("monto a retirar: "))
if(retiro>saldo):
    print("monto no permitido")
elif(retiro>=0):
    saldo=saldo-retiro
    saldocajero=saldocajero-retiro
    print("saldo cuenta=",saldo)
    print("saldo cajero=",saldocajero)