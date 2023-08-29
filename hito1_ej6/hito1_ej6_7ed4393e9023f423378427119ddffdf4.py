#Ordenar tres números
A = eval(input("Ingrese numero: "))

B = eval(input("Ingrese segundo numero: "))

C = eval(input("Ingrese tercer numero: "))



Myor = max(A,B,C)

print("el número mayor es: ", Myor)

Mnor = min(A,B,C)

print("el número menor es: ", Mnor)



P = (A + B + C) - Myor - Mnor



print("El orden de menor a mayor es ", Mnor ," , ", P , " , ", Myor)
