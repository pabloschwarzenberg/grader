#Ordenar tres números
N1 = int(input("Tenga el agrado de ingresar el primer número: "))
N2 = int(input("Tenga el agrado de ingresar el segundo número: "))
N3 = int(input("Tenga el agrado de ingresar el tercer número: "))

if N1 == N2 == N3:
  print("Tenga el agrado de trabajar con valores distintos entre si")
elif N1 < N2 and N2 < N3:
  print  ("sus numeros, en orden de menor a mayor, son", N1,", ", N2, ",", N3)
elif N1 < N3 and N3 < N2: 
  print  ("sus numeros, en orden de menor a mayor, son", N1,", ", N3, ",", N2)
elif N1 < N3 and N3 == N2:
  print  ("sus numeros, en orden de menor a mayor, son", N1,", ", N3, ",", N2)
elif N1 == N3 and N1 < N2:
  print  ("sus numeros, en orden de menor a mayor, son", N1,", ", N3, ",", N2)
elif N2 < N1 and N1 < N3:
  print  ("sus numeros, en orden de menor a mayor, son", N2,", ", N1, ",", N3)
elif N2 < N3 and N3 < N1:
  print  ("sus numeros, en orden de menor a mayor. son", N2,", ", N3, ",", N1),
elif N2 < N3 and N3 == N1:
  print  ("sus numeros, en orden de menor a mayor son", N2,", ", N3, ",", N1)
elif N3 < N1 and N1 < N2:
  print  ("sus numeros, en orden de menor a mayor, son", N3,", ", N1, ",", N2)
elif N3 < N2 and N2 < N1:
  print  ("sus numeros, en orden de menor a mayor, son", N3,", ", N2, ",", N1)
elif N3 < N2 and N2 == N1:
  print  ("sus numeros, en orden de menor a mayor, son", N3,", ", N2, ",", N1)
else:
  print("ERROR, por favor intentelo nuevamente")