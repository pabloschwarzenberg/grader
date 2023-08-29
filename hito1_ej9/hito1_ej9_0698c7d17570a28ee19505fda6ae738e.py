#Sistema de Ecuaciones
def desarollo(a,b,c,d,e,f):
    S = a*e - b*d
    if S !=0:
        x = (c*e - b*f)/S
        y = (a*f - c*d)/S
        print("x=", x, "y=", y)
    else:
        return None, None
a = int(input("Ingrese numero 1:"))
b = int(input("Ingrese numero 2:"))
c = int(input("Ingrese numero 3:"))
d = int(input("Ingrese numero 4:"))
e = int(input("Ingrese numero 5:"))
f = int(input("Ingrese numero 6:"))
print(desarollo(a,b,c,d,e,f))     