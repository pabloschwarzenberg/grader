#Ordenar tres números
n1 = int(input("Ingrese el primer numero entero: "))
n2 = int(input("Ingrese el segundo numero entero: "))
n3 = int(input("Ingrese el tercer numero entreo: "))

if n1 >= n2 >= n3:
    print(n3,",", n2,",", n1)
elif n1 >= n3 >= n2:
    print(n2,",", n3,",", n1)
elif n2 >= n1 >= n3:
    print(n3,",", n1,",", n2)
elif n2 >= n3 >= n1:
    print(n1,",", n3,",", n2)
elif n3 >= n1 >= n2:
    print(n2,",", n1,",", n3)
elif n3 >= n2 >= n1:
    print(n1,",", n2,",", n3)