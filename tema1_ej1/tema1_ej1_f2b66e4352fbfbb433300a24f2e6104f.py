#Suma de los N primeros números
n = int(input("ingrese el numero n: "))
i = 0
total = 0
while i < n:
    natural = n*(n+1)/2
    total += natural
    i += 1
print(natural)
