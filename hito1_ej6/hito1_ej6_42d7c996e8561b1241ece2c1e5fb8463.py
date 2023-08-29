#ordebnar 3 numeros ingresados por el usuario de menor a mayor

#Entrada

n1 = int(input("porfavor ingrese el primer numero: "))
n2 = int(input("porfavor ingrese el segundo numero: "))
n3 = int(input("porfavor ingrese el tercer numero: "))

#procesamiento

if n1 >= n2 and n1 >= n3 and n2 >= n3:
    print(n3,",", n2,",", n1)
if n1 >= n2 and n1 >= n3 and n3 >= n2:
    print(n2,",", n3,",", n1)
if n2 >= n1 and n2 >= n3 and n1 >= n3:
    print(n3,",", n1,",", n2)
if n2 >= n1 and n2 >= n3 and n3 >= n1:
    print(n1,",", n3,",", n2)
if n3 >= n2 and n3 >= n1 and n1 >= n2:
    print(n2,",", n1,",", n3)
if n3 >= n2 and n3 >= n1 and n2 >= n1:
    print(n1,",", n2,",", n3)
      