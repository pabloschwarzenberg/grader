#Cajero Automático
U=10334151
C=1803
SC=1000000
SU=100000
B20=20
B10=40
B5=40
i=1
if i>2:
  print("tarjeta bloqueada") 
else:
  Usuario=input("Ingrese usuario: ")
  Clave=int(input("Ingrese clave: "))
  while i<3:
    if Clave!=C:
      i=i+1
      print("clave invalida")
      Usuario=input("Ingrese usuario: ")
      Clave=int(input("Ingrese clave: "))
      
    else:
      M=int(input("Monto a retirar: "))
      if 0<M<=100000:
        print("saldo cuenta=",SU-M)
        print("saldo cajero=",SC-M,"\n")
        print("billetes 20000=",int(M/20000))
        V20=int(M/20000)
        print("billetes 10000=",int(((M-(V20*20000)))/10000))
        V10=int(((M-(V20*20000)))/10000)
        print("billetes 5000=",int((M-(V10*10000)-(V20*20000))/5000))
        break
      else:
        print("monto no permitido")
  else:
    print("tarjeta bloqueada\n")