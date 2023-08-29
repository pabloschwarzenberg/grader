#Ordenar tres números
numero1 = int(input("ingrese el primer numero entero:"))
numero2 = int(input("ingrese el segundo numero entero:"))
numero3 = int(input("ingrese el tercer numero entero:")) 
 
numeros = [numero1, numero2, numero3]
numeros.sort()
 
numeros_ordenados = ",".join(str(numero) for numero in numeros)
print("numeros ordenados:", numeros_ordenados)