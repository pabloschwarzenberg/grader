#Ordenar tres números
x = int(input('ingrsa un numero '))
s = int(input('ingrsa un numero '))
z = int(input('ingrsa un numero '))

if x<=s and x<=z:
    menor=x
    if s<=z:
        medio=s
        mayor=z
    else:
        medio=z
        mayor=s
        
if s<=x and s<=z:
    menor=s
    if x<=z:
        medio=x
        mayor=z
    else:
        medio=z
        mayor=x

if z<=s and z<=x:
    menor=z
    if s<x:
        medio=s
        mayor=x
    else:
        medio=x
        mayor=s
        
print(str(menor),str(medio),str(mayor))