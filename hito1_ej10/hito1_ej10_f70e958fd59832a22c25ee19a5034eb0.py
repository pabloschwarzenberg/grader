dinero_cajero=1000000
dinero_cliente=100000
cont=0
v=False
while(cont!=3) and (v!=True):
  usuario=int(input("Ingrese usuario: "))
  clave=int(input("Ingrese clave: "))
  if(usuario!=10334151) or (clave!=1803):
    print("clave invalida")
    cont=cont+1
  else:
    retiro=int(input("¿cuanto dinero desea retirar?: "))
    if(retiro>dinero_cliente):
      print("Monto no permitido")
    else:
      dinero_cliente=dinero_cliente-retiro
      dinero_cajero=dinero_cajero-retiro
      print("saldo cuenta: ",dinero_cliente)
      print("saldo cajero: ",dinero_cajero)
      v=True
if(cont==3):
  print("Tarjeta bloqueada")

  
  
      