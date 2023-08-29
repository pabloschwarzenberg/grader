#Cajero Automático
cajero = 1000000

saldo = 100000

usuario = "10334151"

clave = "1803"

usuario1 = input("ingrese su usuario: ")

clave1 = input("ingrese su clave: ")

sw = 0

intentos = 2

salir = "N"

while(intentos>0 and salir=="N"):
  if(usuario == usuario1 and clave == clave1):
    while(sw==0):
      monto = int(input("ingrese el monto a retirar: "))
      if(monto<=saldo):
        saldo = saldo - monto
        cajero = cajero - monto
        print("saldo cuenta=", saldo, "saldo cajero=", cajero)
        salir = input("Si desea hacer otro giro escriba N: ")
        if(salir != "N"):
          sw=1
          
          print("programa finalizado")
      else:
          print("exede saldo maximo")
          monto = int(input("ingrese el monto a retirar: "))
  
  elif(clave!=clave1):
    clave1 = input("clave invalida, ingrese nuevamente la clave: ")
    intentos = intentos-1

if(intentos == 0):
  print("tarjeta bloqueada")