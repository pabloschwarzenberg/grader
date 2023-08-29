#Suma de los N primeros números
total=0
num=int(input("ingrese el numero: "))
n= num*((num+1)/2)

for i in range(0, num+1):
    total= total+i
    
print("la suma del numero de 1 a {} es: ",n)