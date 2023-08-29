X= int(input('Ingrese su primer número: '))
Y= int(input('Ingrese su segundo número: '))
Z= int(input('Ingrese su tercer número: '))

Ma = max(X,Y,Z)
print("el número mayor es: ", Ma)
Mi = min(X,Y,Z)
print("el número menor es: ", Mi)

D = (X + Y + Z) - Ma - Mi

print("De menor a mayor el órden es ", Mi ," , ", D , " , ", Ma) 
