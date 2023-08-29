#Cajero Automático
user=int(input("Ingrese su usuario:"))
psswrd=int(input("Ingrese su clave:"))

trys=1
saldo_c=1000000
saldo_user=100000
person=10334151
contra=1803

b20=20000
b10=10000
b5=5000

def bills(c,x):
    billetes= c // x
    resto= c % x
    return billetes,resto

while psswrd != contra:
    trys += 1

    if psswrd==contra:
       print("Clave incorrecta")
       break

    if trys>3:
       break
    
    print("Clave invalida")
    psswrd=int(input("Ingrese nuevamente su clave:"))

elif trys>3:
   print("Su tarjeta a sido bloqueada")
   
elif user==person:

   if psswrd==contra:
      monto=int(input("Ingrese monto que qiere retirar:"))
       
      if monto > saldo_user and monto > saldo_c:
        print("Monto no permitido")
      else:
         
        saldo_user -= monto
        saldo_c -= monto
        b,r= bills(monto,b20)
        c,r= bills(r,b10)
        j,r= bills(r,b5)
        
        print("Saldo de la cuenta="+str(saldo_user))
        print("Saldo del cajero="+str(saldo_c))
        print("Billetes de 20k="+str(b))
        print("Billetes de 10k="+str(c))
        print("Billetes de 5k="+str(j))