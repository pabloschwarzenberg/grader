#Ordenar tres números
 n1 = input("Ingrese primer numero: ")
n2 = input("Ingrese segundo numero: ")
n3 = input("Ingrese tercer numero: ")

if n1 <= n2 <= n3:
    print(f"{n1},{n2},{n3}")
elif n1 <= n3 <= n2:
    print(f"{n1},{n3},{n2}")
elif n2 <= n1 <= n3:
    print(f"{n2},{n1},{n3}")
elif n2 <= n3 <= n1:
    print(f"{n2},{n3},{n1}")
elif n3 <= n1 <= n2:
    print(f"{n3},{n1},{n2}")
elif n3 <= n2 <= n1:
    print(f"{n3},{n2},{n1}")
    