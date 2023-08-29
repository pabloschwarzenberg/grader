#Entrada
num_1 = eval(input("Ingrese un numero: "))
num_2 = eval(input("Ingrese otro numero: "))
num_3 = eval(input("Ingrese un numero mas: ")) 
#Procesamiento
mayor = max(num_1, num_2, num_3)
menor = min(num_1, num_2, num_3)
medio = (num_1 + num_2 + num_3) - mayor - menor
#Salida
print("El Orden de menor a mayo es:{}, {}, {} ".format(menor,medio,mayor))