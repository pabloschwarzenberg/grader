#Suma de los N primeros números
print('Ingrese el valor final (N)')
a = int(input())
b=0
for i in range(1, a+1):
    print(i)
    b=b+i 
print('La suma es:',b)      