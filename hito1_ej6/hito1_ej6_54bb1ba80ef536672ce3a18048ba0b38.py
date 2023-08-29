x = int(eval(input("Ingrese primer numero: ")))
y = int(eval(input("Ingrese segundo numero: ")))
z = int(eval(input("Ingrese tercer numero: ")))

a = min(x,y,z)
c = max(x,y,z)
b = (x + y + z) - a - c

print (a,",",b,",",c) 