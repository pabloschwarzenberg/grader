#Ordenar tres números
def ordenar_numeros(num1, num2, num3):
    numeros = [num1, num2, num3]  
    numeros.sort()  
    
    
    print(','.join(str(num) for num in numeros))


a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))


ordenar_numeros(a, b, c)