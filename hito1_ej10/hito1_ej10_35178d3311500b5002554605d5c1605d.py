#Cajero Automático
saldo_cajero = 1000000
saldo_usuario = 100000
userExit = True
loops = 0
while userExit:
  usuario = int(input("Ingrese su usuario"))
  clave = int(input("Ingrese su clave"))
  if (usuario ==10334151) and (clave == 1803):
    monto = input("¿Cual es el monto a retirar?")
    if monto.isdigit():
      monto = int(monto)
      if monto < saldo_usuario:
        resto_cajero = saldo_cajero - monto
        resto_usuario = saldo_usuario - monto
        valor1 = "saldo cuenta="+ str(resto_usuario)
        valor2 = "saldo cajero=" + str(resto_cajero)
        lista = []
        lista.append(valor1)
        lista.append(valor2)
        print(lista)
        continuar = input("¿Quiere continuar? Presione N si lo desea")
        if continuar != "N":
          userExit = False          
      else:
        print("monto no permitido")
    else:
      print("monto no permitido")
  else:
    print("clave invalida")
    loops += 1
  if loops == 3:
    print("tarjeta bloqueada")
    userExit = False
