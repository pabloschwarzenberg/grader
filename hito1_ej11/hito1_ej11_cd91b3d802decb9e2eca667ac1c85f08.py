#Cajero automático nivel 2

saldoCuenta=100000
saldoCajero=1000000
bloqueo=0
billetes20000=0
billetes10000=0
billetes5000=0

while True:
  print("***CAJERO AUTOMÁTICO NIVEL 2***")
  print("Para salir ingrese la letra A")
  usuario=input("Usuario: ")
  clave=input("Clave: ")
  if(usuario=="10334151" and clave=="1803"):
    while True:
      print("Saldo disponible: ",saldoCuenta)
      retirar=int(input("Cuánto desea retirar?: "))
      total=saldoCuenta-retirar
      if(total<0):
        print("Está sacando más dinero del que tiene, vuelva a intentarlo")
      else:
        saldoCuenta=saldoCuenta-retirar
        saldoCajero=saldoCajero-retirar
        print("Saldo cuenta: ",saldoCuenta)
        print("Saldo cajero: ",saldoCajero)
        while True:
          if(saldoCuenta>=20000):
            saldoCuenta=saldoCuenta-20000
            billetes20000=billetes20000+1
          elif(saldoCuenta>=10000):
            saldoCuenta=saldoCuenta-10000
            billetes10000=billetes10000+1
          elif(saldoCuenta>=5000):
            saldoCuenta=saldoCuenta-5000
            billetes5000=billetes5000+1
          elif(saldoCuenta==0):
            print("Billetes de 20000: ",billetes20000)
            print("Billetes de 10000: ",billetes10000)
            print("Billetes de 5000: ",billetes5000)
            break
        break
  elif(usuario=="A" or usuario=="a"):
    if(clave=="A" or clave=="a"):
      print("Adiós!")
      break
  else:
    if(bloqueo<3):
      print("Clave inválida")
      bloqueo=bloqueo+1
    else:
      print("Tarjeta bloqueada")
      break
