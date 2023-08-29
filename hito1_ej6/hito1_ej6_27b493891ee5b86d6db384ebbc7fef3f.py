#Ordenar tres números
x1 = int(input("Ingrese el primer número: "))
x2 = int(input("Ingrese el segundo número: "))
x3 = int(input("Ingrese el tercer número: "))

if x3 < x2 and x2 < x1:
  print(x3,",",x2,",",x1)
elif x3 < x1 and x1 < x2:
  print(x3,",",x1,",",x2)
elif x2 < x3 and x3 < x1:
  print(x2,",",x3,",",x1)
elif x2 < x1 and x1 < x3:
  print(x2,",",x1,",",x3)
elif x1 < x2 and x2 < x3:
  print(x1,",",x2,",",x3)
elif x1 < x3 and x3 < x2:
  print(x1,",",x3,",",x2)
elif x1 == x2 and x2 < x3:
  print(x1,",",x2,",",x3)
elif x2 == x3 and x1 < x3:
  print(x1,",",x2,",",x3)
elif x1 == x3 and x1 < x2:
  print(x1,",",x3,",",x2)
elif x1 == x2 and x2 > x3:
  print(x3,",",x2,",",x1)
elif x2 == x3 and x1 > x3:
  print(x3,",",x2,",",x1)
elif x1 == x3 and x1 > x2:
  print(x2,",",x3,",",x1)