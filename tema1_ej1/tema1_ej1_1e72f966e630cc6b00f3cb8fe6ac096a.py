#Suma de los N primeros números
n = int(input("Ingresa un número natural: "))
while (n<0):
   print("el número ingresado no es compatible")
   n = int(input("Ingresa un número: "))
else:
    a = n*(n+1)/2
print("la suma de los primeros n números naturales es: ",a)