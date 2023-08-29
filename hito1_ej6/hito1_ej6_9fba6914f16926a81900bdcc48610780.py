#entrada

print("Ingrese un valor a los numeros para ordenarlos de menor a mayor")

n1 = eval(input("Ingresa tu primer numero: "))
n2 = eval(input("Ingresa tu segundo numero: "))
n3 = eval(input("Ingresa tu tercer numero: "))

#procesamiento

MA = max(n1,n2,n3)

print("el numero mayor es: ", MA)

MI = min(n1,n2,n3)

print("el numero menor es: ", MI)

Z = (n1 + n2 + n3) - MA - MI

#salida

print("De menor a mayor el orden es ", MI ," , ", Z , " , ", MA)