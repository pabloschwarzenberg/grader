#Cajero Automático
      #Cajero Automático
import os
usuario=(input("usuario: "))
clave=int(input("clave: "))
resto1=0
resto2=0
intentos=0
saldo_cajero=1000000
saldo_cuenta=100000
if usuario ==10334151:
      while intentos >=3:
          if clave!=1803:
              print("clave invalida")
          intentos+=1
          if intentos==3:
              print("tarjeta bloqueada")
              os.sistem("cls")
                 
elif clave==1803:
      print("monto a retirar")
      retiro=int(input())
      
      if retiro<=0 or retiro>saldo_cuenta:
          print("monto no permitido")
      if 0<retiro<100000: 
          resto1=saldo_cuenta - retiro
          resto2=saldo_cajero - retiro
          print("saldo cuenta=",resto1,"\nsaldo cajero=",resto2)
          #billetes disponibles:20(x20),10(x40),5(x40)
          veintemil=retiro//200000
          resto20=retiro%20000
          print("billetes 20000=",veintemil)
          if resto20!=0:
            diezmil=retiro//10000
            resto10=retiro%10000
            print("billetes 10000=",diezmil)
            if resto10!=0:
              cincomil=retiro//5000
              print("billetes 5000=",cincomil)
    
          
else:
    print("ingrese usuario correcto")
    
