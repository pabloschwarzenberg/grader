def solucion_sistema_de_ecuaciones(a, b, c, d, e, f):
	
	x = float(c*e-b*f)
	y = float(a*f-c*d)

	print("x="+str(x))
	print("y="+str(y))

x1 = int(input())
x2 = list(str(x1))

a = x2[0]
b = x2[1]
c = x2[2]
d = x2[3]
e = x2[4]
f = x2[5]
a1=int(a)
b1=int(b)
c1=int(c)
d1=int(d)
e1=int(e)
f1=int(f)


print(solucion_sistema_de_ecuaciones(a1, b1, c1, d1, e1, f1))