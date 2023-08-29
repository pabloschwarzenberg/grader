#Suma de los N primeros números
total = 0
num = int(input("Introdusca un Numero:"))

for i in range(0, num+1):
    total = total + i



print("La suma de los numero del 0 al {} es: {}" .format(num, total))