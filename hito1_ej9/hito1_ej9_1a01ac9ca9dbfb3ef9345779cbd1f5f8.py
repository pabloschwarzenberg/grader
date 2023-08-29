a=(float(input("ingrese coeficiente de x: ")))
b=(float(input("ingrese coeficiente de y: ")))
c=(float(input("ingrese resultado: ")))
d=(float(input("ingrese coeficiente de x: ")))
e=(float(input("ingrese coeficiente de y: ")))
f=(float((input("ingrese resultado: "))))


b = b/a
c = c/a
a = a/a

e = e/d
f = f/d
d = d/d

if a*d > 0 :
    g = b-e
    h = c-f
elif a*d < 0:
    g = b+e
    h = c+f
elif a*d == 0:
    print("No se puede resolver")

y = h/g
x = -y*b + c

print("X={0}, Y={1}".format(x,y))
      