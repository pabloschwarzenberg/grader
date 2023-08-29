#Suma de los N primeros números
n= int(input("Ingrese un numero: "))
suma=0
contador= 0
while contador!=n:
    suma= suma + n*(n+1)/2
    print(suma)
    contador= contador + 1
print("El resultado final fue:",suma)      