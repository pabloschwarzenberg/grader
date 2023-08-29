
 #Suma de los N primeros números
n = eval(input("Ingrese cantidad de numeros naturales: "))

if n > 0:
   suma = n+1
   suma2 = suma*n
   suma3 = suma2/2
   print("La suma es",int(suma3))

else:
    print("No se puede realizar la suma")