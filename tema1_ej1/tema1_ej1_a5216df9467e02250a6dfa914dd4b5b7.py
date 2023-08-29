#Suma de los N primeros números
N = int(input("ingrese un numero N natural: "))
suma = N * (N+1)/2
if N < 0:
    print("por  favor ingrese un numero mayor a 0")
else:
    print(suma)