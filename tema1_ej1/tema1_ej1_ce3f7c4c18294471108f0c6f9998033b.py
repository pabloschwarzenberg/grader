#Suma de los N primeros números
def n_numeros(num):
    suma = num*(num+1)/2
    return suma
num = int(input("introduce un numero: "))
print(n_numeros(num))