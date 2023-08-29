#Suma de los N primeros números
n= int(input("ingrese un numero: "))
while not(n>0):
  n= int(input("error...ingrese un numero: "))
suma = n*(n+1)/2
print("la suma de los primeros numeros es: ", n, " el numero es: ", suma)