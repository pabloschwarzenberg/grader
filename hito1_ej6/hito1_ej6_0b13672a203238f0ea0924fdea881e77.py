#Ordenar tres números
X = int(input(" dime el primer numero que elegiste: "))

Y = int(input(" ahora el segundo numero: "))

Z = int(input(" ahora el ultimo numero: "))


Ma = max(X,Y,Z)

Mi = min(X,Y,Z)

C = (X + Y + Z) - Ma - Mi

print("los numeros ordenados de menor a mayor son ", Mi ," , ", C ," , ", Ma)

