#Ordenar tres números
print("**********************")
print("Organizador de Números")
print("**********************\n")

N1 = int(input("Porfavor ingrese el primer número: "))
N2 = int(input("Porfavor ingrese el segundo número: "))
N3 = int(input("Porfavor ingrese el tercer número: "))

if N1 == N2 == N3:
  print("porfavor trabaje con valores que sean distintos entre si")
elif N1 < N2 and N2 < N3:
  print  ("sus numeros ordenados de menor a mayor son", N1,", ", N2, ",", N3)
elif N1 < N3 and N3 < N2: 
  print  ("sus numeros ordenados de menor a mayor son", N1,", ", N3, ",", N2)
elif N1 < N3 and N3 == N2:
  print  ("sus numeros ordenados de menor a mayor son", N1,", ", N3, ",", N2)
elif N1 == N3 and N1 < N2:
  print  ("sus numeros ordenados de menor a mayor son", N1,", ", N3, ",", N2)
elif N2 < N1 and N1 < N3:
  print  ("sus numeros ordenados de menor a mayor son", N2,", ", N1, ",", N3)
elif N2 < N3 and N3 < N1:
  print  ("sus numeros ordenados de menor a mayor son", N2,", ", N3, ",", N1)
elif N2 < N3 and N3 == N1:
  print  ("sus numeros ordenados de menor a mayor son", N2,", ", N3, ",", N1)
elif N3 < N1 and N1 < N2:
  print  ("sus numeros ordenados de menor a mayor son", N3,", ", N1, ",", N2)
elif N3 < N2 and N2 < N1:
  print  ("sus numeros ordenados de menor a mayor son", N3,", ", N2, ",", N1)
elif N3 < N2 and N2 == N1:
  print  ("sus numeros ordenados de menor a mayor son", N3,", ", N2, ",", N1)
else:
  print("hubo un error, intentelo de nuevo mas adelante")