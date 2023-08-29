#Suma de los N primeros números
num1=int(input("ingrese la cantidad de numeros naturales a sumar: "))
tot=0
i=1
while i<=num1:
    tot+=i
    i+=1

print("el total es ",tot)