#Suma de los N primeros números naturales
#La suma de los primeros n numeros naturales está dada por n(n + 1)/2. Crea un programa que reciba como parámetro un número N y luego imprima la suma de los N primeros números naturales

print("Ingresar un Numero : ")
num = int(input())
cont = 0
suma = 0
while cont <= num:
    suma = suma+cont
    cont = cont+1
print("La Suma es : ",suma)

      