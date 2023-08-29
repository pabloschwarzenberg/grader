#Suma de los N primeros números
n = int(input("Ingrese un numero natural:"))
if(n<=0):
   print("Los números negativos no sirven ni el cero tampoco")
else:
    suma = (n*(n+1))/2
    print(suma)