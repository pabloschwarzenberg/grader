#Cajero Automático
saldocajero=1000000
saldocuenta=100000
usuario=10334151
key=1803
usuario=int(input("Ingrese Usuario: "))
contador=1
while contador<=3:
  contraseña=int(input("Ingrese Contraseña :"))
  if (contraseña!=key):
    print("datos Incorrectos, reintente")
    contador=contador+1
    if contador==3:
      print("Clave Bloqueda")
      contador=4
  else:
    contador=4
    giro=int(input("Ingrese Monto a Girar:"))
    if(giro>saldocuenta):
      print("monto no permitido")
    else:
      print("saldo cuenta=",saldocuenta-giro)
      print("saldo cajero=",saldocajero-giro)     