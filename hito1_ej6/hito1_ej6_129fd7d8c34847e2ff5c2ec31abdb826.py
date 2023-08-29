#Ordenar tres números
val_a = int(input("ingrese primer numero: "))
val_b = int(input("ingrese segundo numero: "))
val_c = int(input("ingrese tercer numero: "))

num_menor = min(val_a, val_b, val_c)

num_mayor = max(val_a, val_b, val_c)

num_inter = (val_a + val_b + val_c)-num_mayor-num_menor

print(format(num_menor)+",",format(num_inter)+",",format(num_mayor))