#Cajero Automático
user = input()
key = input()
atm = 1000000
usercash = 100000
attempts = 0
if attempts <3:
  if key == 1803:
    monto = int(input())
    if (monto<=atm and monto<=usercash):
        
        atm = atm-monto
        usercash = usercash -monto
        print("saldo cuenta="+str(usercash))
        print("saldo cajero="+str(atm))
    else:
        print("monto no permitido")
        monto = int(input())      
  else:
    attempts +=1
    
    key = input()

else:
  print("tarjeta bloqueada")
