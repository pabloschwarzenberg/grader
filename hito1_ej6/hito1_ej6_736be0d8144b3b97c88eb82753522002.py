#Ordenar tres números
n1 = int(input("ingrese el primer numero entero: ")) 
n2 = int(input("ingrese el segundo numero entero: "))
n3 = int(input("ingrese el tercer numero entero: "))
if n1 < n2 < n3:
  print("de menor a mayor el orden es: ", n1 , ",", n2 , ",", n3)
elif n1 < n3 < n2:
  print("de menor a mayor el orden es: ", n1 , ",", n3 , ",", n2)
elif n3 < n2 < n1:
  print("de menor a mayor el orden es: ", n3 , ",", n2 , ",", n1)
elif n3 < n1 < n2:
  print("de menor a mayor el orden es: ", n3 , ",", n1 , ",", n2)
elif n2 < n3 < n1:
  print("de menor a mayor el orden es: ", n2 , ",", n3 , ",", n1)
elif n2 < n1 < n3:
  print("de menor a mayor el orden es: ", n2 , ",", n1 , ",", n3)
elif n1 == n2 < n3:
  print("de menor a mayor el orden es: ", n1 , ",", n2 , ",", n3)
elif n1 == n3 < n2:
  print("de menor a mayor el orden es: ", n1 , ",", n3 , ",", n2)
elif n3 == n2 < n1:
  print("de menor a mayor el orden es: ", n3 , ",", n2 , ",", n1)
elif n1 == n2 == n3:
  print("de menor a mayor el orden es: ", n1 , ",", n2 , ",", n3)
elif n1 < n2 == n3:
  print("de menor a mayor el orden es: ", n1 , ",", n2 , ",", n3)
elif n3 < n2 == n1:
  print("de menor a mayor el orden es: ", n3 , ",", n2 , ",", n1)
elif n2 < n3 == n1:
  print("de menor a mayor el orden es: ", n2 , ",", n3 , ",", n1)