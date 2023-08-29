def ordenar_y_imprimir(a, b, c):
    
    numeros = [a, b, c]

   
    numeros.sort()

   
    print(str(numeros[0]) + "," + str(numeros[1]) + "," + str(numeros[2]))


num1 = int(input("Introduzca el primer número: "))
num2 = int(input("Introduzca el segundo número: "))
num3 = int(input("Introduzca el tercer número: "))

ordenar_y_imprimir(num1, num2, num3)
