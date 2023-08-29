#Ordenar tres números
ENT = 3
n = [0.] * ENT
print(n)
print("Indique 3 numeros enteros en cualquier orden:")

for i in range(ENT):
    print(i)
    n[i] = float(input())
 
for i in range(ENT-1):
    for j in range(i+1,ENT):
        if(n[i] > n[j]):
            cambio = n[i]
            n[i] = n[j]
            n[j] = cambio
            
print("Numeros ordenados de menor a mayor:")

for i in range(ENT):
    print(n[i])