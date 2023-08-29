#Cajero Automático
saldo_i = 1000000
account = 100000
intentos = 1
while(intentos <= 3):
  usuario = input("ingrese usuario: ")
  clave = input("ingrese clave: ")
  if (usuario == "10334151" ) and (clave == "1803"):
    print("clave valida")
    monto = eval(input("cual es el monto a retirar: "))
    if (monto < account < saldo_i):
      print("monto permitido")
      cuenta1 = account - monto
      saldo1 = saldo_i - monto
      print("saldo cuenta =",cuenta1)
      print("saldo cajero =",saldo1)
      break
    else:
      print("monto no permitido")
      break

  elif(usuario != "10334151") and (clave != "1803"):
      print("clave invalida")
      intentos = intentos + 1
      if (intentos > 3):
        print("tarjeta bloqueada")