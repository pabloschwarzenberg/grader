#Ordenar tres números
print("Este programa recibe 3 numeros enteros y los ordena de menor a mayor, separados por una coma")
num_1 = int(input("ingresar 1: "))
num_2 = int(input("ingresar 2: "))
num_3 = int(input("ingresar 3: "))

if (num_1 >= num_2 and num_2 >= num_3):
    print(num_3,",",num_2,",",num_1)
elif (num_1 >= num_3 and num_3 >= num_2):
    print(num_2,",",num_3,",",num_1)
elif (num_2 >= num_1 and num_1 >= num_3):
    print(num_3,",",num_1,",",num_2)
elif (num_2 >= num_3 and num_3 >= num_1):
    print(num_1,",",num_3,",",num_2)
elif (num_3 >= num_1 and num_1 >= num_2):
    print(num_2,",",num_1,",",num_3)
elif (num_3 >= num_2 and num_2 >= num_1):
    print(num_1,",",num_2,",",num_3) 
  