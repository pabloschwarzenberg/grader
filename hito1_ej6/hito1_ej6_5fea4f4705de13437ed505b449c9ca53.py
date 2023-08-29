#Ordenar tres números
x = int(input('Ingrese el primer número entero: '))
y = int(input('Ingrese el segundo número entero: '))
z = int(input('Ingrese el tercer número entero: '))

#Menor valor
if x <= y and x <= z:
    N1 = x
elif y <= x and y <= z:
        N1 = y
else: 
    N1 = z
    
#Mayor valor
if x >= y and x >= z:
    N3 = x
elif y >= x and y >= z:
        N3 = y
else:
    N3 = z
    
#Valor intermedio
S = x + y + z
N2 = S - N3 - N1

print('Números en orden ascendente: ', N1, ',', N2,',', N3)     