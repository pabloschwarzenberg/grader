#menor a mayor

n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
n3 = int(input("Ingrese el tercer numero: "))
min = min(n1, n2, n3)
max = max(n1, n2, n3)
med = (n1+n2+n3)-(min+max)
print("El orden de los numero ingresados es: {},{},{}".format(min,med,max))