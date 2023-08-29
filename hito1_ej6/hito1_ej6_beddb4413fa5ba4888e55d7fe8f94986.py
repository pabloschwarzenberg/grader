#Ordenar tres números
n_1 = int(input("Primer número: "))
n_2 = int(input("Segundo número: "))
n_3 = int(input("Tercer número: "))

if n_2 < n_1:
    n_2, n_1 = n_1, n_2
if n_3 < n_2:
    n_3, n_2 = n_2, n_3
if n_2 < n_1:
    n_2, n_1 = n_1, n_2
if n_3 < n_2:
    n_3, n_2 = n_2, n_3
  
print(n_1, n_2, n_3, sep=",")
 