#Sistema de Ecuaciones
a = eval(input("ingrese el valor para a: "))
b = eval(input("ingreese el valor para b: "))
c = eval(input("ingrese el valor para c: "))
d = eval(input("ingrese el valor para d: "))
e = eval(input("ingrese el valor para e: "))
f = eval(input("ingrese el valor para f: "))

det = a * e - b * d

if det != 0 :
    x = (e * c - b * f) / det
    y = (a * f - d * c) / det

    print("x=",(x))

    print("y=",(y))


      