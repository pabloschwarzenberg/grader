saldo_cajero=1000000
saldo_cuenta=100000
intentos=3
clave_invalida=True
usuario_invalido=True



usuario=input("ingrese numero de usuario:")
clave=input("ingrese clave:")

while ((clave_invalida)and(usuario_invalido))and intentos>1:
  if ((clave =="1803")and(usuario=="10334151")):
    clave_invalida=False
    usuario_invalido=False
  if((clave!="1803")and(usuario=="10334151")):
    clave_invalida=True
    intentos=intentos-1
    clave=input("ingrese clave:")
  if((clave=="1803")and(usuario!="10334151")):
    usuario_invalido=True
    print("usuario invalido")
    usuario=input("ingrese numero de usuario:")
      
if ((clave=="1803")and(usuario=="10334151")):
    monto=int(input("ingresa monto a retirar:"))
    if (monto<=100000)and (monto%5000)==0:
     
        saldo_nuevo_cajero=saldo_cajero-monto
        saldo_nuevo_cuenta=saldo_cuenta-monto
        print("Saldo cuenta=",saldo_nuevo_cuenta)
        print("Saldo cajero=",saldo_nuevo_cajero)

        if ((monto<=20000)and((monto%5000)==0)):
              resultado=monto/5000
              print("billetes 20000=",0)
              print("billetes 10000=",0)
              print("billetes 5000=",int(1*resultado))
        
        if ((monto<=50000)and (monto>20000)and((monto%5000)==0)):
              resultado=(monto-30000)/5000
              print("billetes 20000=",1)
              print("billetes 10000=",1)
              print("billetes 5000=",int(1*resultado))

        if ((monto<=100000)and (monto>50000)and((monto%5000)==0)):
              resultado=(monto-60000)/5000
              print("billetes 20000=",2)
              print("billetes 10000=",2)
              print("billetes 5000=",int(1*resultado))
                 
    elif (monto<=100000)and(monto%5000)!=0:
        print("Ingrese un valor que sea multiplo de 5000")
   

    elif(monto>100000):
      print("Saldo insuficiente")
  
else:
  print("tarjeta bloqueada")