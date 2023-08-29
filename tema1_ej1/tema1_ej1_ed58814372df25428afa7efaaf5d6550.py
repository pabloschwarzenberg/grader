#Suma de los N primeros números
num = int(input("Ingrese un numero: ")) 
for i in range(1, num+1): 
    a = [] 
    for x in range(1, i+1): 
        a.append(x)
print(sum(a)) 