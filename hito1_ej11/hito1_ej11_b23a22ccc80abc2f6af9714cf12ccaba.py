#Cajero Automático
usuario=int(input("ingrese numero de usuario:"))
clave=1803
while(clave>1802 or clave<1984):
  clave=(int(input("ingresa tu clave:")))
  if(clave==1803):
    monto=100000
    while(monto>99999):
      monto=int(input("¿Cuál es su monto a retirar?:"))
      if(monto>100000):
        print("monto no permitido")
        monto=int(input("¿Cuál es su monto a retirar?:"))
      if(monto<100001):
        scu=(100000-monto)
        sca=(1000000-monto)
        print("saldo cuenta=",scu)
        print("saldo cajero=",sca)
        if(monto==10000):
          b2=5
          b1=0
          b5=0
          print("billetes 20000=",b2)
          print("billetes 10000=",b1)
          print("billetes 5000=",b5)
        else:  
          b2=0
          b1=(monto%100000)//10000
          b5=(monto%10000)//1000
          print("billetes 20000=",b2)
          print("billetes 10000=",b1)
          print("billetes 5000=",b5)
  
        break
  else:
    (clave!=1803)
    print("clave invalida")
    clave=(int(input("ingresa tu clave:")))  
    if(clave!=1803):
      print("clave invalida")
    clave=(int(input("ingresa tu clave:")))  
    if(clave!=1803):
      print("tarjeta bloqueada")
  break 