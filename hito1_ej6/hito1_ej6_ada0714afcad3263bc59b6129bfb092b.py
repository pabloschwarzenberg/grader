x = eval(input("Ingrese un numero: "))
y = eval(input("Ingrese un segundo numero: "))
z = eval(input("Ingrese un tercer numero: "))

a = max(x,y,z)
c = min(x,y,z)

b = (x + y + z) - a - c

print("De menor a mayor el órden es ", c ," , ", b , " , ", a)
      