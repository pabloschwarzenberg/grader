#Ordenar tres números
x1 = int(input("Ingrese primer numero: "))
x2 = int(input("Ingrese segundo numero: "))
x3 = int(input("Ingrese tercer numero: "))

a = min(x1,x2,x3)
b = max(x1,x2,x3)
c = (x1+x2+x3)-a-b

print("los mumeros ordenados de menor a mayor", (a,c,b))