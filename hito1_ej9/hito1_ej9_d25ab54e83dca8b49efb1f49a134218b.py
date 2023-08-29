a = float(input("Inserte el valor de A:"))
b = float(input("Inserte el valor de  B:"))
c = float(input("Inserte el valor de C:"))
d = float(input("Inserte el valor de D:"))
e = float(input("Inserte el valor de E:"))
f = float(input("Inserte el valor de F:"))


x = (c * e - b * f) // (a * e - b * d)
y = (a * f - c * d) // (a * e - b * d)

print("x=" +str(x) + "y="+str(y))