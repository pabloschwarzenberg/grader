#Ordenar tres números
X = eval(input("Ingrese un numero: "))

Y = eval(input("Ingrese un segundo numero: "))

Z = eval(input("Ingrese un tercer numero: "))

# El end sirve para printar 2 veces en la misma linea
#El max encuentra el numero más grande dentro de los ()
#El min lo mismo pero con el minimo.

Ma = max(X,Y,Z)

Mi = min(X,Y,Z)

print("Maximo y minimo", end=" ")

print("el número mayor es: ", Ma, end="")

print("el número menor es: ", Mi)



D = (X + Y + Z) - Ma - Mi



print("De menor a mayor el órden es ", Mi ," , ", D , " , ", Ma) 
      