#Ordenar tres números
#Escribe un programa que reciba tres números enteros y los imprima ordenados de menor a mayor, separados por una coma.


awarded = []
for i in range(3):
    awarded.append(int(input("Ingresa un número: ")))
awarded.sort()
print("Los números  son " + str(awarded))  
    