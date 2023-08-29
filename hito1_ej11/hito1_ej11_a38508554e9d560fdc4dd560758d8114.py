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
      b20k = int(monto/20000)
      monto = monto%20000
      b10k = int(monto/10000)
      monto = monto%10000
      b5k = int(monto/5000)
      monto = monto%5000
      print("billetes 20000 =",b20k)
      print("billetes 10000 =",b10k)
      print("billetes 5000 =",b5k)
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
        print("tarjeta bloqueada")      