#Suma de los N primeros números
N = int(input("ingrese un numero natura: "))
suma = N*(N+1)/2
if N > 0:
    print(suma)
else:
    print("este numero es erroneo")