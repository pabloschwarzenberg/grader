numeros= [] 
for i in range(3):
    numero=int(input("ingrese un numero"))
    numeros.append(numero)
    
numeros.sort()
print(numeros[0],",",numeros[1] ,",",numeros[2] )
    