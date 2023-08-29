#Ordenar tres números
n_1 = eval(input("ingrese su primer numero"))
n_2 = eval(input("ingrese su segundo numero"))
n_3 = eval(input("ingrese su tercer numero"))
#Proceso
MA = max(n_1, n_2, n_3)
MI = min(n_1, n_2, n_3)
F = (n_1 + n_2 + n_3) - MA - MI
#Salida
print("El orden de menor a mayor es:", MI , " , " , F , " , " , MA)