#Ordenar tres números
numeros=[]
for i in range(3):
    numero=int(input("Ingrese un numero:"))
    numeros.append(numero)   
numeros.sort()
print(numeros[0],",",numeros[1],",",numeros[2])
