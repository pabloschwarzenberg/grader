#Cajero Automático
saldocajero=1000000
usuario=10334151
clavereal=1803
saldousuario=100000

usuario=int(input("ingrese un numero de usuario:",))
intentos=0
while intentos<2:
  clave=int(input("Ingrese clave:"))
  intentos=intentos+1
  if clave!=clavereal:
    print("clave invalida, ingrese nuevamente")
  if clave==clavereal:
    break
if clave==clavereal:
  print("cual es el monto que desea retirar?")
  monto=str(input())
  x=int((monto))
  saldonuevousuario=(100000-x)
  saldonuevocajero=(1000000-x)
  
  if x>100000:
    print("monto no permitido")
  elif x<=100000:
    print("saldo cuenta=",saldonuevousuario)
    print("saldo cajero=",saldonuevocajero)
if clave!=clavereal:
  print("Tarjeta bloqueada")