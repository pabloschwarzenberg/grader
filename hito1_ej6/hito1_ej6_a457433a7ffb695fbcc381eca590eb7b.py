print("Escribe un programa que reciba tres números enteros y los imprima ordenados de menor a mayor, separados por una coma")
a = int(input("Ingrese primer numero: "))
b = int(input("Ingrese segundo numero:"))
c = int(input("Ingrese tercer numero: "))
z = (min(a, b, c))
w = (max(a, b, c))
y = ((a + b + c) - z - w)
print(z,y, w,sep=",")