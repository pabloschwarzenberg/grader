#Cajero Automático
saldo_inicial = 1000000
cuenta = 100000
intento = 1
while(intento <= 3):
  usuario = input("ingrese usuario: ")
  clave = input("ingrese clave: ")
  if (usuario == "10334151" ) and (clave == "1803"):
    print("clave valida")
    monto = eval(input("cual es el monto a retirar: "))
    if (monto < cuenta < saldo_inicial):
      print("monto permitido")
      cuenta1 = cuenta - monto
      saldo1 = saldo_inicial - monto
      print("saldo cuenta =",cuenta1)
      print("saldo cajero =",saldo1)
      break
    else:
      print("monto no permitido")
      break

  elif(usuario != "10334151") and (clave != "1803"):
      print("clave invalida")
      intento = intento + 1
      if (intento > 3):
        print("tarjeta bloqueada")     