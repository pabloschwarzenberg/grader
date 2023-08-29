valor1 = int(input("Ingresa el 1° número: "))
valor2 = int(input("Ingresa el 2° número: "))
valor3 = int(input("Ingresa el 3° número: "))

if valor1 <= valor2 <= valor3:
  print((valor1),",",(valor2),",",(valor3))
elif valor1 <= valor3 <= valor2:
  print((valor1),",",(valor3),",",(valor2))
elif valor2 <= valor1 <= valor3:
  print((valor2),",",(valor1),",",(valor3))
elif valor2 <= valor3 <= valor1:
  print((valor2),",",(valor3),",",(valor1))
elif valor3 <= valor1 <= valor2:
  print((valor3),",",(valor1),",",(valor2))
elif valor3 <= valor2 <= valor1:
  print((valor3),",",(valor2),",",(valor1))