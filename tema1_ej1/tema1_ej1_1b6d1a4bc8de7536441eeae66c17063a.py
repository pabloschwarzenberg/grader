#Suma de los N primeros números
a=int(input("ingrese un numero"))
contador= 1
suma=0
while(contador <= a):
    suma = suma + contador
    contador = contador + 1
print(suma)