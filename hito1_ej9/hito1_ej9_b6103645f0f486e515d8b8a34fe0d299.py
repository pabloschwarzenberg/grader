a = float(input("ingrece: "))
b = float(input("ingrece: "))
c = float(input("ingrece: "))
d = float(input("ingrece: "))
e = float(input("ingrece: "))
f = float(input("ingrece: "))

det = a * e - b * d

if det != 0 :
    x = (e * c - b * f) / det
    y = (a * f - d * c) / det

    print("La solucion al sistema es: ")
    print("x=","{:.1f}".format((x)))
    print("y=","{:.1f}".format((y)))
          