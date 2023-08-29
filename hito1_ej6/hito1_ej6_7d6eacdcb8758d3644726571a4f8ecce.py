 
a = input("Ingrese el primer numero: ")
b = input("Ingrese el segundo numero: ")
c = input("Ingrese el tercer numero: ")
a = int(a)
b = int(b)
c = int(c)
num1=0
num2=0
num3=0

if a>=b and a>=c:
    num1 = a
    a = b
    b = c
elif b>=a and b>=c:
    num1 = b
    b = c
elif c>=a and c>=b:
    num1 = c
else:
    print("Se ha generado un error")

if a>=b:
    num2 = a
    num3 = b
elif b>=a:
    num2 = b
    num3 = a
else: 
    print("Se ha generado un error")

print(str(num3)+","+str(num2)+","+str(num1)) 