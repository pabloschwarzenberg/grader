#Cajero Automático
veintemil=20
diezmil=40
cincomil=40
saldo=100000
saldocajero=veintemil*20000+diezmil*10000+cincomil*5000

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
    
if(clave==1803):
 retiro=int(input("monto a retirar: "))
 if(retiro>saldo):
    print("monto no permitido")
 elif(retiro>=0):
    cincomil=cincomil-retiro/5000

    saldo=saldo-retiro
    saldocajero=saldocajero-retiro
    print("saldo cuenta=",saldo)
    print("saldo cajero=",saldocajero)
    print("billetes 20000=0")
    print("billetes 10000=0")
    print("billetes 5000=",retiro//5000)

      