#Ordenar tres números
     
      numeros.sort()
      #indicar que son 3 numeros
      numeros = [num1, num2, num3]
      numeros_ordenados = ', '.join(str(num) for num in numeros)
      return numeros_ordenados
#ingresa los numeros      
numero1 = int(input("Ingrese un numero: ")) 
numero2 = int(input("Ingrese un numero: "))
numero3 = int(input("Ingrese un numero: "))
#ordenar los 3 x numeros
resulado = ordenar_numero(numero1, numero2, numero3)
#otorgar un resultado
print("Sus numeros en orden son: "+resultados)
      