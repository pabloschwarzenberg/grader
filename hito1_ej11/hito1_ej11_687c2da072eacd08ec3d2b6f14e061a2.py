#Cajero Automático
saldoinicial = 1000000
cuenta = 100000
intento = 1
while(intento <= 3):
  usuario = input("ingrese usuario: ")
  clave = input("ingrese clave: ")
  if (usuario == "10334151" ) and (clave == "1803"):
    print("clave valida")
    monto = eval(input("cual es el monto a retirar: "))
    if (monto < cuenta < saldoinicial):
      print("monto permitido")
      cuenta1 = cuenta - monto
      saldo1 = saldoinicial - monto
      b20 = int(monto/20000)
      monto = monto%20000
      b10 = int(monto/10000)
      monto = monto%10000
      b5 = int(monto/5000)
      monto = monto%5000
      print("billetes 20000 =",b20)
      print("billetes 10000 =",b10)
      print("billetes 5000 =",b5)
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