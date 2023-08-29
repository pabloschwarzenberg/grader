saldo_inicial=100000
scajero_inicial=1000000
#billetes cajero
caj20=int(20)
caj10=int(40)
caj5=int(40)
#billetes usuario
us20=0
us10=0
us5=0
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
  us20= caj20 -(caj20 - (monto//20000))
  us10= caj10 -(caj10 - (monto-(us20*20000))//10000)
  monto=(monto-((us20*20000)+(us10*10000)))
  us5= caj5 -(caj5 - (monto//5000))
  
  print("Saldo cuenta={}".format(saldo_inicial))
  print("Saldo cajero={}".format(scajero_inicial))
  print("Billetes 20000={}".format(us20))
  print("Billetes 10000={}".format(us10))
  print("Billetes 5000={}".format(us5))
  stop=input("Si desea continuar presione la tecla N: ")
      