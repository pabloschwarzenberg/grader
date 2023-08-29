numero1 = int(input("Ingrese un número: "))

numero2 = int(input("Ingrese un segundo número: "))

numero3 = int(input("Ingrese un tercer número: "))

a = max(numero1,numero2,numero3)

b = min(numero1,numero2,numero3)

c = (numero1 + numero2 + numero3) - a - b

print("Los números ordenados son: ", b ," , ", c , " , ", a)
      