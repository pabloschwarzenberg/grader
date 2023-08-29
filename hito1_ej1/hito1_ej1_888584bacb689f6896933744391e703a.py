#Nota final
contador = 0
suma = 0
numero = 1

while numero != 0:
    numero = int(input("Colque sus notas: "))
    if numero != 0:
        suma += numero
        contador += 1
if contador == 0:
    print ("No coloco la nota correctamente.")
else:
    promedio = suma / contador
    print(" El promedio de sus {} notas equivalen a {} de promedio.". format(contador, promedio))