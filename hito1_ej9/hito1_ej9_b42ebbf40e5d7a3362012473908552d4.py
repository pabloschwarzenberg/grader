#Sistema de Ecuaciones
a=int(input("Ingrese el primer valor :"))
b=int(input("Ingrese el segundo valor :"))
c=int(input("Ingrese el tercer valor :"))
d=int(input("Ingrese el cuarto valor :"))
e=int(input("Ingrese el quinto valor :"))
f=int(input("Ingrese el sexto valor :"))

def SE(a,b,c,d,e,f):
    det = a * e - b * d

    if det != 0:
        x = (c * e - b * f) / det
        y = (a * f - c * d) / det

        return x
        #print("x="+x,"y="+y)
    else:
        return None, None
def SE2(a,b,c,d,e,f):
    det = a * e - b * d

    if det != 0:
        x = (c * e - b * f) / det
        y = (a * f - c * d) / det

        return y
        
    else:
        return None, None
print("x =",SE(a,b,c,d,e,f))
print("y =",SE2(a,b,c,d,e,f))

   