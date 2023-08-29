#Cajero Automático
saldo_inicial=100000
scajero_inicial=1000000
usuario = 0
clave = 0
intentos=0      #contador
while usuario!=10334151:
  usuario=int(input("Ingrese numero de cuenta: "))
while clave != 1803 and intentos!=3:
  clave=int(input("Ingrese clave de la cuenta: "))
  if clave != 1803:
    print("Clave invalida")
    intentos+=1
    print("Le quedan", 3-intentos ,"intento(s).")
if intentos==3:
  print("Tarjeta bloqueada")
  exit()
stop="N"
while stop=="N" and saldo_inicial!=0:
  monto=scajero_inicial + 1
  while monto > scajero_inicial and monto > saldo_inicial:
      monto=int(input("Ingrese monto a retirar: "))
      if monto > scajero_inicial and monto > saldo_inicial:
          print("Monto no permitido")
  saldo_inicial-=monto
  scajero_inicial-=monto
  print("Saldo cuenta={}".format(saldo_inicial))
  print("Saldo cajero={}".format(scajero_inicial))
  stop=input("Si desea continuar presione la tecla N: ")
