x = int(input("ingrese el valor del primer numero: "))
y = int(input("ingrese el valor del segundo numero: "))
z = int(input("ingrese el valor del tercer numero: "))

a = min(x,y,z)
c = max(x,y,z)
b = (x+y+z)-a-c

print("los numeros ordenados son : {} , {}, {}".format (a,b,c))