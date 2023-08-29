#Ordenar tres números
      x = int("Escribe el primer numero: ")
      y = int("Escribe el segundo numero: ")
      z = int("Escribe el tercer numero: ")
      
      a = min(x, y, z)
      c = max(x, y, z)
      b = (x + y + z) - a - c
      
      print("Los numeros ordenados son: " ,a, b, "y", c