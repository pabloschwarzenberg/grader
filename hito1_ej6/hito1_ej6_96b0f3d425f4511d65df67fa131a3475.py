#Ordenar tres números
num_1 = int(input("Ingrese el primero numero: "))
num_2 = int(input("Ingrese el segundo numero: "))
num_3 = int(input("Ingrese el tercer numero: "))

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

      