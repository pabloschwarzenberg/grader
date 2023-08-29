#Ordenar tres números
num_1 = int(input("Ingrese el primer número:\n"))
num_2 = int(input("Ingrese el segundo número:\n"))
num_3 = int(input("Ingrese el tercer número:\n"))
orden = [num_1,num_2,num_3]
orden.sort()
print(str(orden [0])+","+str(orden[1])+","+str(orden[2]))