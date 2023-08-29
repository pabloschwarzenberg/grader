#Contestador de celular
print ("Ingrese número telefónico:")
n=int(input())
a=int(n%1000)
b=int(n//100000)
print ("Ingrese hora de la llamada (n° positivo entre 0 y 23):")
h=int(input())
if h > 23:
   print ("¡Debes ingresar un número positivo ENTRE 0 y 23!")
if h < 0:
   print ("¡Debes ingresar un número POSITIVO entre 0 y 23!")
if 0 <= h <= 7:
    print ("CONTESTAR")
if 7 < h < 14:
   if a == 909:
      print ("CONTESTAR")
   else:
      print ("NO CONTESTAR")
if 14 <= h < 17:
   print ("NO CONTESTAR")
if 17 <= h <= 19:
   if b == 877:
      print ("NO CONTESTAR")
   else:
      print ("CONTESTAR")
if h > 19:
   print ("NO CONTESTAR")
   

      