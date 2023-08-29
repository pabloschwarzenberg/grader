#Cajero Automático
while True:
  usuario=int(input("usuario: "))
  clave1=int(input("clave: "))
  if usuario!=10334151:
    continue
  if clave1!=1803:
    print("clave invalida")
    clave2=int(input("clave: "))
    if clave2!=1803:
      print("clave invalida")
      clave3=int(input("clave: "))
      if clave3!=1803:
        print("tarjeta bloqueada")
        continue
  montoretira=int(input("monto a retirar:" ))
  if montoretira>100000:
    print("monto no permitido")
    continue
  scuenta=100000-montoretira
  scajero=1000000-montoretira
  print("saldo cuenta= ",scuenta,",","saldo cajero= ",scajero)
  nuevaoperacion=input("para una nueva operación marque la letra N")
  N=int(1)
  if nuevaoperacion==1:
    continue
  else:
    break
print("Gracias por su operación")
      
  
      
  