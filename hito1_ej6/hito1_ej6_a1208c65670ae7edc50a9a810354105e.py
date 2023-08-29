#Ordenar tres números
n_1 = int(input("Ingresa el primer número: "))
n_2 = int(input("Ingresa el segundo número: "))
n_3 = int(input("Ingresa el tercer número: "))
while True:
    if n_1 <= n_2 and n_1<= n_3:
        menor = n_1
        if n_2 <= n_3:
            medio = n_2
            mayor = n_3
        else:
            medio = n_3
            mayor = n_2
    elif n_2 <= n_1 and n_2 <= n_3:
        menor = n_2
        if n_1 <= n_3:
            medio = n_1
            mayor = n_3
        else:
            medio = n_3
            mayor = n_1
    else:
        menor = n_3
        if n_1 <= n_2:
            medio = n_1
            mayor = n_2
        else:
            medio = n_2
            mayor = n_1
    break
print("Números ordenados:", menor,",", medio,",", mayor)