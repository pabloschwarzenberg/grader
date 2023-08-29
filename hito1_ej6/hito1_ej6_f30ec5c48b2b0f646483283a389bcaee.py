#Ordenar tres números
n1 =int(input("Ingrese primer valor"))
n2 =int(input("Ingrese segundo valor"))
n3 =int(input("Ingrese tercer valor"))

a = min (n1, n2, n3)
c = max (n1, n2, n3)
b = (n1 + n2+ n3)- a - c
print("Los numeros ordenados de mayor a menor son",(a,b,c))