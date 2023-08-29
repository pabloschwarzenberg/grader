#Ordenar tres números
a=int(input("Introduzca el primer número: "))
b=int(input("Introduzca el segundo número: "))
c=int(input("Introduzca el tercer número: "))
if a<=b<=c:
   print(str(a) + "," + str(b) + "," + str(c))
if a<=c<=b:
   print(str(a) + "," + str(c) + "," + str(b))
if b<=a<=c:
   print(str(b) + "," + str(a) + "," + str(c))
if b<=c<=a:
   print(str(b) + "," + str(c) + "," + str(a))
if c<=a<=b:
   print(str(c) + "," + str(a) + "," + str(b))
if c<=b<=a:
   print(str(c) + "," + str(b) + "," + str(a))
   
   