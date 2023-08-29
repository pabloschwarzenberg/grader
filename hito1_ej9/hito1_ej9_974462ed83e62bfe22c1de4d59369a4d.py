a = float(input("Ingrese un número para A: "))
b = float(input("Ingrese un número para B: "))
c = float(input("Ingrese un número para C: "))
d = float(input("Ingrese un número para D: "))
e = float(input("Ingrese un número para E: "))
f = float(input("Ingrese un número para F: "))


x = (c * e - b * f) // (a * e - b * d)
y = (a * f - c * d) // (a * e - b * d)

print("x=" +str(x) + "y="+str(y))