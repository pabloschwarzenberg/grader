#Ordenar tres números


num1 = eval(input("Ingrese un numero: "))
num2 = eval(input("Ingrese un segundo numero: "))
num3 = eval(input("Ingrese un tercer numero: "))


Ma = max(num1,num2,num3)
Mi = min(num1,num2,num3)
D = (num1 + num2 + num3) - Ma - Mi

# Salida
print("Maximo y minimo", end=" ")
print("el número mayor es: ", Ma, end=" ")
print("el número menor es: ", Mi)

print("De menor a mayor el órden es ", Mi ," , ", D , " , ", Ma)