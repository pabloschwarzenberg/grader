#Ordenar tres números
X = eval(input("Ingrese un numero: "))
Y = eval(input("Ingrese un segundo numero: "))
Z = eval(input("Ingrese un tercer numero: "))

Ma = max(X,Y,Z)
Mi = min(X,Y,Z)
print("Maximo y minimo", end=" ")
print("el número mayor es: ", Ma, end="")
print("el número menor es: ", Mi)

D = (X + Y + Z) - Ma - Mi

print("De menor a mayor el órden es ", Mi ," , ", D , " , ", Ma) 
      