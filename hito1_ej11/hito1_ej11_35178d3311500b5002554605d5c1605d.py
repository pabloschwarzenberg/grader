#Cajero Automático
saldo_cajero = 1000000
saldo_usuario = 100000
twenty_bils = 20
ten_bills = 40
five_bills = 40
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
        billetes_de_veinte = monto//20000
        resto_de_veinte = monto%20000
        print("billetes 20000=",billetes_de_veinte)
        if resto_de_veinte != 0:
          billetes_de_diez = resto_de_veinte//10000
          print("billetes 10000=",billetes_de_diez)
        else:
          print("billetes 10000=",0)
        resto_de_diez = monto%10000
        if resto_de_diez != 0:
          billetes_de_cinco = resto_de_diez//5000
          print("billetes 5000=",billetes_de_cinco)
        else:
          print("billetes 5000=",0)        
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
