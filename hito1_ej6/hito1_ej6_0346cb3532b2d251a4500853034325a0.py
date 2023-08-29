#Ordenar tres números
def numeros(a, b, c):
    numeros = [a, b, c]  
    numeros.sort()  


    print(", ".join(str(num) for num in numeros))

num_1 = int(input("Ingrese el primer número: "))
num_2 = int(input("Ingrese el segundo número: "))
num_3 = int(input("Ingrese el tercer número: "))


numeros(num_1, num_2, num_3)