#Ordenar tres números
def imprimir_numeros_ordenados(num1, num2, num3): 
    numeros = [num1, num2, num3] 
    numeros.sort() 
    numeros_ordenados = ', '.join(map(str, numeros)) 
    print(numeros_ordenados) 
   
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))
  
imprimir_numeros_ordenados(numero1, numero2, numero3)