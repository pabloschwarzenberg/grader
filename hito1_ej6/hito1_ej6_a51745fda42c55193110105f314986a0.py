#Ordenar tres números
TAM = 3
num = [0] * TAM
 
for i in range(TAM):
    num[i] = int(input("Ingrese Numero "))
 
for i in range(TAM-1):
    for j in range(i+1,TAM):
        if(num[i] > num[j]):
            cambio = num[i]
            num[i] = num[j]
            num[j] = cambio
 
print(num[0],",",num[1],",",num[2])