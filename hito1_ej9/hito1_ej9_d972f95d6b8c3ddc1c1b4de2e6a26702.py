#Sistema de Ecuaciones
      
a1 = float(input("Numero 1 = "))
b1 = float(input("Numero 2 = "))
c1 = float(input("Numero 3 = "))
a2 = float(input("Numero 1.2 = "))
b2 = float(input("Numero 2.2 = "))
c2 = float(input("Numero 3.2 = "))

if a1/a2 == b1/b2 and b1/b2 == c1/c2:
    print("Infinitas soluciones")
    
elif a1/a2 == b1/b2 and b1/b2 != c1/c2:
    print("No tiene solución")
    
else:
    x = (c1*b2-c2*b1) / (a1*b2-a2*b1)
    y = (a1*c2-a2*c1) / (a1*b2-a2*b1)
    print("x=" , round(x,1))
    print("y=" , round(y,1))
