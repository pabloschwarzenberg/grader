#Descomponer un número
numero= int(input("Introduce el número: "))
umil = numero / 1000
tmp = numero % 1000

centenas = tmp / 100
tmp = tmp % 100

decenas = tmp / 10
unidades = tmp % 10
if numero<10:
   print("Unidad: %i" % unidades)  
elif numero<100:
   print ("Decena: %i" % decenas)
   print("Unidad: %i" % unidades)
elif numero<1000:
   print ("Centena: %i" % centenas)
   print ("Decena: %i" % decenas)
   print("Unidad: %i" % unidades)
elif numero>999:
   print ("Milesima: %i" % umil)
   print ("Centena: %i" % centenas)
   print ("Decena: %i" % decenas)
   print("Unidad: %i" % unidades)
else: print("")
