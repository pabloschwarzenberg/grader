#Cajero Automático
dic_usuarios = {"10334151":"1803"}
dic_plata_cajero = {"10334151":1000000}
saldo_cuenta = {"10334151":100000}

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
        
        if retiro < dic_plata_cajero[usuario]:
          dic_plata_cajero[usuario] -= retiro
          saldo_cuenta[usuario] -= retiro
          print("[saldo cuenta =", saldo_cuenta[usuario], ",","saldo cajero = ", dic_plata_cajero[usuario],"]")
    


          aux = True

        else:
          retiro = int(input("Cantidad de retiro es mayor al fondo del cajero, reeintente: "))
         

  continuar = input("Quiere salir?: ")        