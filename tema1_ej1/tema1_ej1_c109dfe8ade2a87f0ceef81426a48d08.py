#Suma de los N primeros números
N = int(input("Ingrese un numero: "))
if N>0:
    resultado = (N*(N+1))/2
    print(f"su resultado es: {resultado}")
else:
    print("Ingrese un numero mayor a 0")
