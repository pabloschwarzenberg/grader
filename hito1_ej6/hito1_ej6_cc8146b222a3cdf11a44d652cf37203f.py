valor1 = int(input("Ingrese el valor 1: "))
valor2 = int(input("Ingrese el valor 2: "))
valor3 = int(input("Ingrese el valor 3: "))

if valor1 >= valor2 >= valor3:
  mayor = valor1
  mayor_intermedio = valor2
  menor = valor3
  print(menor, ",", mayor_intermedio, ",", mayor)

elif valor1 >= valor3 >= valor2:
  mayor = valor1
  mayor_intermedio = valor3
  menor = valor2
  print(menor, ",", mayor_intermedio, ",", mayor)

elif valor2 >= valor1 >= valor3:
  mayor = valor2
  mayor_intermedio = valor1
  menor = valor3
  print(menor, ",", mayor_intermedio, ",", mayor)

elif valor2 >= valor3 >= valor1:
  mayor = valor2
  mayor_intermedio = valor3
  menor = valor1
  print(menor, ",", mayor_intermedio, ",", mayor)

elif valor3 >= valor1 >= valor2:
  mayor = valor3
  mayor_intermedio = valor1
  menor = valor2
  print(menor, ",", mayor_intermedio, ",", mayor)

elif valor3 >= valor2 >= valor1:
  mayor = valor3
  mayor_intermedio = valor2
  menor = valor1
  print(menor, ",", mayor_intermedio, ",", mayor)