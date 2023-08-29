#Cajero Automático
user=int(input("Ingrese su usuario:"))
psswrd=int(input("Ingrese su clave:"))

trys=1
saldo_c=1000000
saldo_user=100000
person=10334151
contra=1803

while psswrd != contra:
    trys += 1

    if psswrd==contra:
       print("Clave incorrecta")
       break

    if trys>3:
       break
    
    print("Clave invalida:")
    psswrd=int(input("Ingrese nuevamente su clave:"))

if trys>3:
   print("Su tarjeta a sido bloqueada")
   
if user==person:

   if psswrd==contra:
      monto=int(input("Ingrese monto que qiere retirar:"))
       
      if monto> saldo_user and monto> saldo_c:
        print("Monto no permitido")
      else:
         
        saldo_user==monto
        saldo_c==monto
        
        print("Saldo de la cuenta="+str(saldo_user))
        print("Saldo del cajero="+str(saldo_c))