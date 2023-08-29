#Sistema de Ecuaciones
a = int(input("a ="))
b = int(input("b ="))
c = int(input("c ="))
d = int(input("d ="))
e = int(input("e ="))
f = int(input("f ="))
x = 1
y = 2
incognita2 = a*f-c/b+a*e
incognita = c-b*incognita2*((a*f-c)/b+a*e)
print("el valor de x es: ",x ,"y el valor de y es: ",incognita2 )