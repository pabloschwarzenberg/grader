#Ordenar tres números
print("Introduce 3 números enteros")
numeros = [int(input("Número 1: ")), int(input("Número 2: ")), int(input("Número 3: "))]
#Proceso
contador = 0 
while(len(numeros) > contador):
    contador_interno = 0   
    while(len(numeros) > contador_interno):
        if(numeros[contador] < numeros[contador_interno]):
            numeros[contador_interno], numeros[contador] = numeros[contador], numeros[contador_interno]       
        contador_interno = contador_interno + 1    
    contador = contador + 1
print(numeros)  