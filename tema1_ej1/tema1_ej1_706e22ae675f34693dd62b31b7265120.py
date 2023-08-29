#Suma de los N primeros números
 # Entrada

N = int(input("Ingrese un numero: "))

if N < 0:
    print("Vuelva a ingresar un numero: ")

# Calculo de la Solucion

if N > 0:
    sol = N*(N + 1) / 2
    print("La solucion es", sol)

#Fin
print("Fin.")     