#Entrada
n_1 = int(input("Escriba el primer número: "))
n_2 = int(input("Escriba el segundo número: "))
n_3 = int(input("Escriba el tercer número: "))

#Procesamiento 
if n_1 <= n_2 and n_2 <= n_3:
    print("el orden ascendente es:", n_1,"," ,n_2,",", n_3)
elif n_1 <= n_3 and n_3 <= n_2:
    print("el orden ascendente es:",n_1,"," ,n_3,",", n_2)
elif n_2 <= n_1 and n_1 <= n_3:
    print("el orden ascendente es:", n_2,"," ,n_1,",", n_3)
elif n_2 <= n_3 and n_3 <= n_1:
    print("el orden ascendente es:", n_2,"," ,n_3,",", n_1)
elif n_3 <= n_1 and n_1 <= n_2:
    print("el orden ascendente:", n_3,"," ,n_1,",", n_2)
elif n_3 <= n_2 and n_2 <= n_1:
    print("el orden ascendente es:", n_3,"," ,n_2,",", n_1)

      