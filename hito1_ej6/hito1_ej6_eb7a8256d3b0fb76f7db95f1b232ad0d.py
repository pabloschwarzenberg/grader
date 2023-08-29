#Ordenar tres números
x = eval(input("primer número:"))
y = eval(input("segundo número:"))
z = eval(input("tercer número:"))

a = min(x, y, z)
c = max(x, y, z)
b = (x + y + z)- a - c



print(a,",",b,",",c)
     
      