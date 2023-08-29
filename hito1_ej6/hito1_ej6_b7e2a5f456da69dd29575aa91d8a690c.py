#Ordenar tres números
print("Ordenar tres números de menor a mayor")
num_1=int(input("Ingrese número 1: "))
num_2=int(input("Ingrese número 2: "))
num_3=int(input("Ingrese número 3: "))
num_menor=min(num_1,num_2,num_3)
num_mayor=max(num_1,num_2,num_3)
num_medio= (num_1+num_2+num_3)-num_mayor-num_menor
print("Los números ordenados son:{}, {}, {}".format(num_menor,num_medio,num_mayor))