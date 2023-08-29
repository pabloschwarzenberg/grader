#Ordenar tres números
x = int(input("Escriba el primer número: "))
y = int(input("Escriba el segundo número: "))
z = int(input("Escriba el tercer número: "))

nmin = min(x, y, z)
nmax = max(x, y, z)
nint = (x + y + z) - nmin - nmax

print("Los números de menor a mayor son:  {}, {} , {}".format(nmin, nint, nmax))