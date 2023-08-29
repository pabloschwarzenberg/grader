#Sistema de Ecuaciones


a = float(input("Digite Numero para A:"))
b = float(input("Digite Numero para B:"))
c = float(input("Digite Numero para C:"))
d = float(input("Digite Numero para D:"))
e = float(input("Digite Numero para E:"))
f = float(input("Digite Numero para F:"))


x = (c * e - b * f) // (a * e - b * d)
y = (a * f - c * d) // (a * e - b * d)

print("x=" +str(x) + "y="+str(y))