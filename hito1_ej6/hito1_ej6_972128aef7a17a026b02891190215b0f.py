#Ordenar tres números
a = int(input("ingrese un numero:"))
b = int(input("ingrese segundo numero:"))
c = int(input("ingrese un tercer numero"))
MA = max(a, b, c)
MI = min(a, b, c)
D = (a + b + c) - MA - MI
print("de menor a mayor el orden es", MI , "," , D , "," , MA)
