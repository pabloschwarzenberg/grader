#Entradas
print("ordenar números de menor a mayor")
#Números
num_un = int(input("El primer número es: "))
num_do = int(input("El segundo número es: "))
num_tr = int(input("El tercer número es: "))
#Ecuación
if num_un <= num_do and num_do <= num_tr :
    print(num_un,",",num_do,",",num_tr)
elif num_un <= num_tr and num_tr <= num_do :
    print(num_un,",",num_tr,",",num_do)
elif num_do <= num_un and num_un <= num_tr :
    print(num_do,",",num_un,",",num_tr)
elif num_do <= num_tr and num_tr <= num_un :
    print(num_do,",",num_tr,",",num_un)
elif num_tr <= num_do and num_do <= num_un :
    print(num_tr,",",num_do,",",num_un)
elif num_tr <= num_un and num_un <= num_do :
    print(num_tr,",",num_un,",",num_do)
else:
    print("Número no es entero")