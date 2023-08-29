print("Ax+By=C")
print("Dx+Ey=F")
a=float(input("ingrese el valor de X en la primera ecuacion:\n"))

z=float(input("ingrese el valor de Y en la primera ecuacion:\n"))

r=float(input("ingrese el valor de C en la primera ecuacion:\n"))

a2=float(input("ingrese el valor de X en la segunda ecuacion:\n"))

b2=float(input("ingrese el valor de Y en la segunda ecuacion:\n"))

r2=float(input("ingrese el valor de C en la segunda ecuacion:\n"))

n = a * b2 - z * a2
if n != 0:
    u1 = (r * b2 - z * r2) / n
    o1 = (a * r2 - r * a2) / n
print("X=",round(u1, 2))
print("y=",round(o1, 2))