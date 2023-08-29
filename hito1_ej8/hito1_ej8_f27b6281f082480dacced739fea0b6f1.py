num = int(input("Ingrese un número de hasta 4 dígitos: "))

 

if num > 999:

   miles = num // 1000

   num %= 1000

   print(str(miles) + "M", end="")

 

if num > 99:

   centenas = num // 100

   num %= 100

   print(" + " + str(centenas) + "C", end="")

 

if num > 9:

   decenas = num // 10

   num %= 10

   print(" + " + str(decenas) + "D", end="")

 

if num > 0:

   unidades = num

   print(" + " + str(unidades) + "U", end="") 