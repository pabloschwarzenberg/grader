x = int(input("ingrese su primer número: "))

y = int(input("ingrese su segundo número: "))

z = int(input("ingrese su tercer número: "))

Mi = min(x,y,z)

Ma = max(x,y,z)

b = (x + y + z) - Ma - Mi

print("De menor a mayor el órden es ", Mi ," , ", b , " , ", Ma)