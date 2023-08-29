#Cajero Automático
cajero = 1000000

billete20 = 20

billete20e = 0

billete10 = 40

billete10e = 0

billete5 = 40

billete5e = 0

giro = 0

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
    monto = int(input("ingrese el monto a retirar: "))
    while(sw==0):
      if(monto<=saldo):
        saldo = saldo - monto
        cajero = cajero - monto
        print("saldo cuenta=", saldo, "saldo cajero=", cajero)
        while(monto!=giro):
          if(monto>=giro + 20000 and billete20>0):
            giro = giro + 20000
            billete20 = billete20 - 1
            billete20e = billete20e + 1
          elif(monto>=giro + 10000 and billete10>0):
            giro = giro + 10000
            billete10 = billete10 - 1
            billete10e = billete10e + 1
          elif(monto>=giro + 5000 and billete5>0):
            giro = giro + 5000
            billete5 = billete5 - 1
            billete5e = billete5e + 1
        print(billete20e*20000+billete10e*10000+billete5e*5000)
        print("billetes 20000= ",billete20e)
        print("billetes 10000= ",billete10e)
        print("billetes 5000= ",billete5e)
        salir = input("Si desea hacer otro giro escriba N: ")
        if(salir != "N"):
          sw=1
          print("programa finalizado") 
        else:
          billete20e = 0
          billete10e = 0
          billete5e = 0
          giro = 0
          monto = int(input("ingrese el monto a retirar: "))
           
      else:
        print("exede saldo maximo")
        monto = int(input("ingrese el monto a retirar: "))
        
            

  
  elif(clave!=clave1):
    clave1 = input("clave invalida, ingrese nuevamente la clave: ")
    intentos = intentos-1

if(intentos == 0):
  print("tarjeta bloqueada")