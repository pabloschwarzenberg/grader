
      #Ordenar tres números
  # Entrada

X = eval(input("Ingrese un numero: "))
Y = eval(input("Ingrese un segundo numero: "))
Z = eval(input("Ingrese un tercer numero: "))

#Procesamiento
Ma = max(X,Y,Z)
Mi = min(X,Y,Z)
D = (X + Y + Z) - Ma - Mi

# Salida
print("Maximo y minimo", end=" ")
print("el número mayor es: ", Ma, end=" ")
print("el número menor es: ", Mi)

print("De menor a mayor el órden es ", Mi ," , ", D , " , ", Ma)