#Suma de los N primeros números
a = int(input('Dame un numero: '))
sumar = 0
for a in range(1,a+1):
    sumar += a
    a += 1
print(sumar)

