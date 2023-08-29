#Suma de los N primeros números
ne = int(input("ingrese un número: "))
i = 0
n =''
while ne > i:
    n = ne*(ne + 1)/2
    n = int(n)
    i += 1

print(n)