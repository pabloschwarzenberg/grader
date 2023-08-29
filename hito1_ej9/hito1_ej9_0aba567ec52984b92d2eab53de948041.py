a = int(input("Coloque un numero 1:"))
b = int(input("Coloque un numero 2:"))
c = int(input("Coloque un numero 3:"))
d = int(input("Coloque un numero 4:"))
e = int(input("Coloque un numero 5:"))
f = int(input("Coloque un numero 6:"))

def solucion(a,b,c,d,e,f):
    det = a*e - b*d
    if det !=0:
        x = (c*e - b*f)/det
        y = (a*f - c*d)/det
        
        print("x=", x, "y=", y)
    else:
        return None, None
        
print(solucion(a,b,c,d,e,f))