#Ordenar tres números

print("Hoy ordenaremos 3 numeros de menor a mayor")

a = eval(input("Ingrese primer número: "))
b = eval(input("Ingrese segundo numero: "))
c = eval(input("Ingrese tercer numero: "))

if (a <= b <= c):
    abc = a,+b,+c    
    print("El orden de menor a mayor es: ", abc)

elif (a <= c <= b):
    acb = a,+c,+b   
    print("El orden de menor a mayor es: ", acb)


elif (b <= a <= c):
    bac = b,+a,+c   
    print("El orden de menor a mayor es: ", bac)

elif (b <= c <= a):
    bca = b,+c,+a   
    print("El orden de menor a mayor es: ", bca)

elif (c <= a <= b):
    cab = c,+a,+b   
    print("El orden de menor a mayor es: ", cab)

elif (c <= b <= a):
    cba = c,+b,+a   
    print("El orden de menor a mayor es: ", cba)