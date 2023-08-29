#Suma de los N primeros números
a = int(input('Ingrese un numero: '))
s = 0
i = 0
while i < a:
    i += 1
    s += i
    print(s, end=' ')    