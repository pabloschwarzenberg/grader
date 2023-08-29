#Ordenar tres números
Numero1 = int(input(" Ingrese el primer numero: "))
Numero2 = int(input(" Ingrese el segundo numero: "))
Numero3 = int(input(" Ingrese el tercer numero: "))

NumMenor = min(Numero1, Numero2, Numero3)
NumMayor = max(Numero1, Numero2, Numero3)
NumMid = (Numero1 + Numero2 + Numero3) - NumMenor - NumMayor

print("Los numeros ordenados de menor a mayor son: " + str(NumMenor) + ", " + str(NumMid) + ", " + str(NumMayor))