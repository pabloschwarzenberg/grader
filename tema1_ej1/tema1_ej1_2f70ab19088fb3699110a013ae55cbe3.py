#Suma de los N primeros números
print("Debe ingresar un numero N paracalcular la suma")
print("de los n pimeros numeros naturales")
N = eval(input("Ingrese N: "))
r=N*(N + 1)/2
if N>0:
    print("La suma de los n primeros numeros naturales de", N, " es:", r)
else:
    print("opcion no valida") 
      