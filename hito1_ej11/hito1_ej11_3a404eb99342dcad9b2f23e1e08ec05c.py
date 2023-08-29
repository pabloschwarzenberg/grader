
def billetes(pedido):
 for w_20 in range(0,20):
  for w_10 in range(0,40):
   for w_5 in range(0,40):
    suma=w_20*20+w_10*10+w_5*5
    if(suma==pedido):
         return {"20K":w_20,"10K":w_10,"5K":w_5}
 return False


dicc={"20K":20,"10K":40,"5K":40}
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
      if(monto>100000 or billetes(monto/1000)==False):
         print("monto no permitido")
     print("saldo cuenta=",saldo_cuenta-monto)
     print("saldo cajero=",saldo_cajero-monto)     
     billetes=billetes(monto/1000)
     print("billetes 20000=",billetes["20K"])
     print("billetes 10000=",billetes["10K"])
     print("billetes 5000=",billetes["5K"])
     h=input("")
     if(h!="N"):
         break
 if(input_!=1803):
     z=z+1
if(z==3):print("tarjeta bloqueada") 
      