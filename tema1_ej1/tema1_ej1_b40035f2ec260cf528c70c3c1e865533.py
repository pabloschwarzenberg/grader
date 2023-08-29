#Suma de los N primeros números
num1 = int(input("ingresar numero: "))

for numero in range(1,num1+1,1):
    print((numero*(numero+1))/2)