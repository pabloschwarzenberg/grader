#Ordenar tres números
X = int(input(" primer numero : "))

Y = int(input(" segundo numero : "))

Z = int(input(" tercer numero : "))


Ma = max(X,Y,Z)

Mi = min(X,Y,Z)

C = (X + Y + Z) - Ma - Mi

print("los numeros ordenados de menor a mayor son ", Mi ," , ", C ," , ", Ma)


