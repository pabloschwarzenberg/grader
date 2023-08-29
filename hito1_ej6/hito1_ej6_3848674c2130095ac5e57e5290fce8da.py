#Ordenar tres números
n1=int(input("Ingrese el primer digito: "))
n2=int(input("Ingrese el segundo digito: "))
n3=int(input("Ingrese el tercer digito: "))

minimo = min(n1,n2,n3)
maximo = max(n1,n2,n3)
medio = n1 + n2 + n3 - minimo - maximo

print(minimo,",",medio,",",maximo)