def solucion(a,b,c,d,e,f):
    det = a*e - b*d
    if det !=0:
        x = (c*e - b*f)
        y = (a*f - c*d)
        print("x=", x, "y=",y)
    else:
        return None, None
a = int(input("ingrese num 1: "))
b = int(input("ingrese num 2: "))
c = int(input("ingrese num 3: "))
d = int(input("ingrese num 4: "))
e = int(input("ingrese num 5: "))
f = int(input("ingrese num 6: "))
print(solucion(a,b,c,d,e,f))