#Ordenar tres números
      x=int(input("Ingresa el primer numero"))
      y=int(input("Ingresa el segundo numero"))
      z=int(input("Ingresa el tercer numero"))
      
      numeros_ordenados = [x, y, z]
        numeros_ordenados = [numero1, numero2, numero3]
        numeros_ordenados.sort()

      # Imprimir los números ordenados
      print("Los números ordenados de menor a mayor son:", end=" ")
      for i in range(len(numeros_ordenados)):
        print(numeros_ordenados[i], end="")
            if i < len(numeros_ordenados) - 1:
              print(",", end=" ")
      
      