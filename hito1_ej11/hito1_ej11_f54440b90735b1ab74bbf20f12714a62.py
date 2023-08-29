#Cajero Automático
dic_usuarios = {"10334151":"1803"}
dic_plata_cajero = {"10334151":1000000}
saldo_cuenta = {"10334151":100000}
billetes = {20000:20, 10000:40, 5000:40}


continuar = "N"
while continuar == "N":
  usuario = input("Ingrese su usuario: ")
  clave = input("Ingrese su clave: ")
  intentos = 0

  if usuario not in dic_usuarios and usuario not in dic_plata_cajero:
    dic_usuarios[usuario] = clave
    dic_plata_cajero[usuario] = 1000000
    saldo_cuenta[usuario] = 0
  
  elif usuario in dic_usuarios and usuario in dic_plata_cajero:
    while clave != dic_usuarios[usuario] and intentos < 3:
      intentos += 1
      clave = input("Clave invalida, por favor reintente: ")
      if intentos == 3:
        print("Tarjeta bloqueada")
        continuar = "S"

    if dic_usuarios[usuario] == clave:
      aux = False
      while aux != True:
        retiro = int(input("Cuanto quiere retirar?: "))
        
        if retiro < dic_plata_cajero[usuario] and retiro % 5000 == 0:
          dic_plata_cajero[usuario] -= retiro
          saldo_cuenta[usuario] -= retiro

          print("Saldo cuenta = ", saldo_cuenta[usuario], ", ", "saldo cajero = ", dic_plata_cajero[usuario])
          
          billetes_20 = 0
          billetes_10 = 0
          billetes_5 = 0
          
          suma = 0
          while retiro != 0:
            if retiro // 20000 >= 1 and billetes[20000] > 0:
              billetes_20 += retiro // 20000 - 1
              suma += ((retiro // 20000) - 1) * 20000 
              billetes[20000] -= billetes_20
              retiro = (retiro % 20000) + 20000

            elif retiro // 10000 >= 1 and billetes[10000] > 0:
              billetes_10 += retiro // 10000 - 1
              suma += ((retiro // 10000) - 1) * 10000
              billetes[10000] -= billetes_10
              retiro = (retiro % 10000) + 10000

            elif retiro // 5000 >= 1 and billetes[5000] > 0:
              billetes_5 += retiro // 5000
              suma += (retiro // 5000) * 5000
              billetes[5000] -= billetes_5
              retiro = retiro % 5000
            else:
               retiro = int(input("Cantidad de retiro es mayor al fondo del cajero, reeintente: "))
          print("billetesde20000:", billetes_20)
          print("billetesde10000:", billetes_10)
          print("billetesde5000:", billetes_5
              
          


  continuar = input("Quiere salir?: ")