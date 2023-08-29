#Ordenar tres números

x = int(input("Ingresa primer numero: "))
y = int(input("Ingresa segundo numero: "))
z = int(input("Ingresa tercer numero: "))

if x > y and y > z:
    print(z,",",y,",", x)

if y > x and x > z:
    print(z,",",x,",",y)

if z > x and x > y:
    print(y,",",x,",",z)
 
if x > z and z > y:
    print(y,",",z,",",x)

if z > y and y > x:
    print(x,",",y,",",z)

if y > z and  z > x:
    print(x,",",z,",",y)

if x==z and z==y:
  print("Todos los numeros son iguales")

if x == y and y > z:
  print(z,",",y,",",x)
  if x == y and y > z:
    print(z,",",y,",",x)

if y==z and z>x:
  print(x,",",z,",",y)
  if y==z and z<x:
    print(z,",",y,",",x)

if x==z and x>y:
  print(y,",",x,",",z)
  if x==z and x>y:
    print(x,",",z,",",y)