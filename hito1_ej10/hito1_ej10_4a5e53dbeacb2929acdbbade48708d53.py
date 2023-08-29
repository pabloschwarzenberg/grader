#Cajero Automático
saldo_cajero=1000000
saldo_cuenta=100000
monto=saldo_cuenta+1
z=0
h="N"
usuario=input("nombre usuario ")
while(z!=3 and h=="N"):
 if(3>z>0):
     print("clave invalida")
 input_=int(input("escriba clave "))
 if(input_==1803):
    while True: 
     while(monto>100000):
      monto=int(input("¿cuanto desea retirar? "))
      if(monto>100000):
         print("monto no permitido")
     print("saldo cuenta=",saldo_cuenta-monto)
     print("saldo cajero=",saldo_cajero-monto)
     h=input("")
     if(h!="N"):
         break
 if(input_!=1803):
     z=z+1
if(z==3):print("tarjeta bloqueada")     