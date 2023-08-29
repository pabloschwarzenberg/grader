#Ordenar tres números
#Entradas
num_1 = int(input("Favor ingresa un numero entero: "))
num_2 = int(input("Favor ingresa un segundo numero entero: "))
num_3 = int(input("Favor ingresa un tercer numero entero: "))

#Desarrollo
if num_1 <= num_2 and num_2 <= num_3:
    print(num_1,"," ,num_2,",", num_3)
elif num_1 <= num_3 and num_3 <= num_2:
    print(num_1,"," ,num_3,",", num_2)
elif num_2 <= num_1 and num_1 <= num_3:
    print(num_2,"," ,num_1,",", num_3)
elif num_2 <= num_3 and num_3 <= num_1:
    print(num_2,"," ,num_3,",", num_1)
elif num_3 <= num_1 and num_1 <= num_2:
    print(num_3,"," ,num_1,",", num_2)
elif num_3 <= num_2 and num_2 <= num_1:
    print(num_3,"," ,num_2,",", num_1)
