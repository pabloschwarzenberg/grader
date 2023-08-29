#Ordenar tres números
a = int(input("ingrese un numero:"))
b = int(input("ingrese segundo numero:"))
c = int(input("ingrese tercer numero:"))
MA = max(a, b, c)
MI = min(a, b, c)
D = (a + b + c) - MA - MI
print("Sus numeros ordenados de menor a mayor son", MI , "," , D , "," , MA)
