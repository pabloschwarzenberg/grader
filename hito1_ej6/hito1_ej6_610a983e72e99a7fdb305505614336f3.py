#Ordenar tres números
numeros=[]
for i in range(3):
    numeros.append(int(input('ingrese un numero entero: ')))
numeros.sort()
print(numeros[0],numeros[1],numeros[2],sep=',')
