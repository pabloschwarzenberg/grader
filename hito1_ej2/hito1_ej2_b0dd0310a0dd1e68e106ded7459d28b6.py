#Contestador de celular
numero=int(input("Hola, ingrese su número de teléfono de ocho dígitos para reconocerlo: "))
numeroinicial=int(numero//100000)
numerofinal=int(numero%1000)
while numero<10000000:
         print("El número de teléfono debe ser de ocho dígitos")
         numero=int(input("Ingrese su número de teléfono de ocho dígitos: "))
while numero>99999999:
         print("El número de teléfono debe ser de ocho dígitos")
         numero=int(input("Ingrese su número de teléfono de ocho dígitos: "))
hora=int(input("Ahora, ingrese la hora (0-23) en la que está llamando: "))
while hora>23:
      print("No es correcta la hora ingresada. Inténtelo nuevamente")
      hora=int(input("Ingrese la hora (0-23) actual: "))
while hora<0:
      print("No es correcta la hora ingresada. Inténtelo nuevamente")
      hora=int(input("Ingrese la hora (0-23) actual: "))
if 0<=hora<=7:
    print("CONTESTAR")
elif 7<hora<14:
    if numerofinal==909: 
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif 14<hora<17:
      print("NO CONTESTAR")
elif 17<=hora<=19:
      if numeroinicial==877:
        print("NO CONTESTAR")
      else:
        print("CONTESTAR")
else:
      print("NO CONTESTAR")      