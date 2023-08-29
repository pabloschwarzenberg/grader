#Ordenar tres números

Numero1 = int(input("Introduce el primer número: "))
Numero2 = int(input("Introduce el segundo número: "))
Numero3 = int(input("Introduce el tercer número: "))

NumeroMayor = max(Numero1, Numero2, Numero3)
NumeroMenor = min(Numero1, Numero2, Numero3)
NumeroMedio = (Numero1 + Numero2 + Numero3) - NumeroMayor - NumeroMenor

print("Los números ordenados de menor a mayor son:", NumeroMenor, ",", NumeroMedio, ",", NumeroMayor)