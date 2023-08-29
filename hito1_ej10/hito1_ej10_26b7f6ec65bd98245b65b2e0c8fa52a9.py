usuario=int(input())
clave=int(input())
saldo_cajero=1000000
saldo_usuario=100000
i=0
N=1
while(N==1):
  while(clave!=1803) and (i<3):
    print("clave invalida")
    i=i+1
  if(clave!=1803):
    print("tarjeta bloqueada")
  elif(usuario==10334151) and (clave==1803):
    monto=int(input())
    if(monto<=100000):
      saldo_usuario=saldo_usuario-monto
      saldo_cajero=saldo_cajero-monto
      print("saldo cuenta=", saldo_usuario)
      print("saldo cajero=", saldo_cajero)
    elif(monto>100000):
      print("monto no permitido")
  n=input("ingrese algo distinto a N para salir")