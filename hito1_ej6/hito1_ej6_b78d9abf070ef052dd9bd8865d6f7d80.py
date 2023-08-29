#Ordenar tres números
x = int(input("escriba un primer numero: "))
y = int(input("escriba un segundo numero: "))
z = int(input("escriba un tercer numero: "))

a = min(x,y,z)
c = max(x,y,z)
b = (x+y+z)-a-c

print("los numeros de menor a mayor son: {}, {} y {}".format(a, b, c))