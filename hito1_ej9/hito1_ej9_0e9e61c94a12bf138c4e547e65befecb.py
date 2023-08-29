#Sistema de Ecuaciones
a= int(input("ingerse el valor a: "))
b= int(input("ingerse el valor b: "))
c= int(input("ingerse el valor c: "))
d= int(input("ingerse el valor d: "))
e= int(input("ingerse el valor e: "))
f= int(input("ingerse el valor f: "))
divisor = a * e - b * d

if divisor != 0 :
    x = (e * c - b * f) / divisor
    y = (a * f - d * c) / divisor

    print("La solucion al sistema es x= %s e y= %s" % (x, y))



