#Suma de los N primeros números
#Matías
n=int(input("Ingrese un valor natural: ", ))
if n<0:
  print("Ese numero no es natural")
a= int(n*(n + 1)/2)
print(a, ",", a+1, ",", a+2, ",",a+3)
