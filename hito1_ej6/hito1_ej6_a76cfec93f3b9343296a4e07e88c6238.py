#Ordenar tres números
n1=int(input("primer numero: "))
n2=int(input("segundo numero: "))
n3=int(input("tercer numero: "))

numeros = (n1,n2,n3)
ordenados= sorted(numeros)
print("los numeros de menor a mayor son:")
print(ordenados)