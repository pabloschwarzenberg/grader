#Suma de los N primeros números
n= int(input('ingresa un numero '))
total=0
for i in range(n):
    n=(n+1)/2
    total=total + n
    print(total)