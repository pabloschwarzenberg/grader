#Ordenar tres números
a = eval(input("Ingrese el primer numero entero: "))
b = eval(input("Ingrese el segundo numero entero: "))
c = eval(input("Ingrese el tercer numero entero: "))
NumMenor = min(a,b,c)
NumMayor = max(a,b,c)
NumMedio = (a + b + c) - (NumMayor + NumMenor)
print("El orden de estos numeros de menor a mayor es: {0}, {1}, {2}" .format(NumMenor,NumMedio,NumMayor))
