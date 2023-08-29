#Ordenar tres números

x = int(input("Ingrese primer numero: "))
y = int(input("Ingrese segundo numero: "))
z = int(input("Ingrese tercer numero: "))

a = min(x,y,z)
c = max(x,y,z)
b = (x + y + z) - a - c

if a == b:
  print(a,",",a,",",c)
elif c == b:
  print(a,",",c,",",c)
else:
  print(a,",",b,",",c)





